# ============================================VARIABLES===========================================
BOT_DIR		= bot
DOCS_DIR	= docs
SCRIPTS_DIR	= scripts
TESTS_DIR	= tests

CONT			= docker-compose.yaml
DB_CONT			= docker-compose.db.yaml
ALEMBIC_CONT	= docker-compose.alembic.yaml
# ============================================VARIABLES===========================================

# ==============================================CODE==============================================
.PHONY: lint
lint:
	isort --check-only $(BOT_DIR)
	black --check --diff $(BOT_DIR)
	ruff $(BOT_DIR)

.PHONY: reformat
reformat:
	black $(BOT_DIR)
	isort $(BOT_DIR)
	ruff --fix $(BOT_DIR)
# ==============================================CODE==============================================

# =============================================DOCKER=============================================
.PHONY: up bot
up db:
	docker-compose -f $(CONT) up -d

.PHONY: down bot
down db:
	docker-compose -f $(CONT) down

.PHONY: up db
up db:
	docker-compose -f $(DB_CONT) up -d

.PHONY: down db
down db:
	docker-compose -f $(DB_CONT) down

.PHONY: up migrations
up db:
	docker-compose -f $(ALEMBIC_CONT) up -d

.PHONY: down migrations
down db:
	docker-compose -f $(ALEMBIC_CONT) down
# =============================================DOCKER=============================================