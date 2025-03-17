import unittest
import tempfile
import os
import json
from unittest.mock import patch, MagicMock

from src import data_persistence
from src import github_integration
from src import scheduler
from src import config


class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        # Create a temporary file name to test save/load functions.
        self.temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        self.temp_file_name = self.temp_file.name
        self.temp_file.close()  # We'll manage writing/reading separately.

    def tearDown(self):
        # Clean up the temporary file if it exists.
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    def test_save_and_load_game_state(self):
        # Define a sample game state.
        game_state = {
            "turn": 5,
            "board": "test_board_state",
            "votes": {"e2e4": 3, "d2d4": 2},
            "teams": {"white": ["Alice", "Bob"], "black": ["Charlie", "Dana"]}
        }
        # Save the game state to the temporary file.
        data_persistence.save_game_state(
            game_state, filename=self.temp_file_name)
        # Load the game state from the temporary file.
        loaded_state = data_persistence.load_game_state(
            filename=self.temp_file_name)
        self.assertEqual(game_state, loaded_state)

    def test_load_nonexistent_file(self):
        # Provide a file name that does not exist.
        non_existent_file = "nonexistent_file.json"
        if os.path.exists(non_existent_file):
            os.remove(non_existent_file)
        loaded_state = data_persistence.load_game_state(
            filename=non_existent_file)
        self.assertEqual(loaded_state, {})


class TestGithubIntegration(unittest.TestCase):
    @patch('github_integration.Github')
    def test_commit_update_existing_file(self, MockGithub):
        # Create a fake repo and fake file contents object.
        fake_repo = MagicMock()
        fake_contents = MagicMock()
        fake_contents.path = "game_state.json"
        fake_contents.sha = "fake_sha"
        fake_repo.get_contents.return_value = fake_contents
        instance = MockGithub.return_value
        instance.get_repo.return_value = fake_repo

        # Create a temporary file to simulate the game state file.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tf:
            tf.write('{"turn": 1, "board": "test_board"}')
            temp_file_name = tf.name

        # Call the commit function (simulate update scenario).
        github_integration.commit_game_state_to_github(
            token="fake_token",
            repo_name="fake/repo",
            file_path=temp_file_name,
            commit_message="Test commit update"
        )

        # Check that update_file was called with correct parameters.
        fake_repo.update_file.assert_called_once_with(
            fake_contents.path,
            "Test commit update",
            '{"turn": 1, "board": "test_board"}',
            fake_contents.sha
        )
        os.remove(temp_file_name)

    @patch('github_integration.Github')
    def test_commit_create_new_file(self, MockGithub):
        # Simulate an exception when get_contents is called to force creation of a new file.
        fake_repo = MagicMock()
        fake_repo.get_contents.side_effect = Exception("File not found")
        instance = MockGithub.return_value
        instance.get_repo.return_value = fake_repo

        # Create a temporary file to simulate the game state file.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tf:
            tf.write('{"turn": 2, "board": "another_board"}')
            temp_file_name = tf.name

        # Call the commit function (simulate create new file scenario).
        github_integration.commit_game_state_to_github(
            token="fake_token",
            repo_name="fake/repo",
            file_path=temp_file_name,
            commit_message="Test commit create"
        )

        # Check that create_file was called with correct parameters.
        fake_repo.create_file.assert_called_once_with(
            temp_file_name,
            "Test commit create",
            '{"turn": 2, "board": "another_board"}'
        )
        os.remove(temp_file_name)


class TestScheduler(unittest.TestCase):
    # Use patch.object to override config constants during this test.
    @patch.object(config, 'GITHUB_TOKEN', "fake_token")
    @patch.object(config, 'REPO_NAME', "fake/repo")
    @patch.object(config, 'GAME_STATE_FILE', "game_state.json")
    @patch('github_integration.commit_game_state_to_github')
    def test_scheduled_commit(self, mocked_commit):
        # Call the scheduled_commit function and ensure it calls commit_game_state_to_github correctly.
        scheduler.scheduled_commit()
        mocked_commit.assert_called_once_with(
            token="fake_token",
            repo_name="fake/repo",
            file_path="game_state.json",
            commit_message="Automated commit of game state"
        )


if __name__ == '__main__':
    unittest.main()
