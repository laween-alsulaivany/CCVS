.PHONY: cron install uninstall python_instance chess_install chess_uninstall

cron: ## Run `make cron install` or `make cron uninstall`
	@echo "Use 'make cron install' to add or 'make cron uninstall' to remove the cron job."

install:
	@./add_cron_job.sh

uninstall:
	@./remove_cron_job.sh

python_instance: ## Install custom Python
	@./chess_python_installer.sh

chess_install: ## Create /usr/bin/chess symlink
	@./install_chess_cmd.sh

chess_uninstall: ## Remove /usr/bin/chess symlink
	@./uninstal_chess_cmd.sh

