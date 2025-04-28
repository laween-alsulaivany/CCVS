.PHONY: cron install uninstall python_instance chess_install chess_uninstall

cron: ## Run `make cron install` or `make cron uninstall`
	@echo "Use 'make cron install' to add or 'make cron uninstall' to remove the cron job."

cron-install:
	@./scripts/add_cron_job.sh --home-dir="$(HOME_DIR)"

install:
	@./scripts/add_cron_job.sh

uninstall:
	@./scripts/remove_cron_job.sh

python_instance: ## Install custom Python
	@./scripts/chess_python_installer.sh

chess_install: ## Create /usr/bin/chess symlink
	@./scripts/install_chess_cmd.sh

chess_uninstall: ## Remove /usr/bin/chess symlink
	@./scripts/uninstall_chess_cmd.sh

