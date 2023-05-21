# Trader
App for monitoring the exchange rate and cryptocurrency


## TODO
 - [ ] Complete telegram bot  
   - [ ] Refactor code
   - [ ] Make tech support
   - [ ] Write an admin system
   - [ ] Make models
   - [ ] Make schemas 
   - [ ] Make CRUD requests
   - [ ] 
   - [ ] 

 - [ ] Complete auto-tests
   - [ ] bot auto-tests
   - [ ] api auto-tests

- [ ] Migrations 
   - [ ] Make alembic init file
   - [ ] 
   - [ ] 

 - [ ] DevOps
   - [X] Dockerfiles 
   - [X] Docker-compose yamls
   - [ ] 
   - [ ] 

 - [ ] Database
   - [ ] 
   - [ ] 

- [ ] Cache
   - [ ] Redis

## API
### Frameworks
 - FastAPI
 - 

##### *currently in the development phase*


## Telegram bot
### Frameworks
 - Aiogram (currently 2.x.x)
 - 


## Style guide
 - [PEP-8](https://peps.python.org/pep-0008/)
 - SOLID
 - KISS
 - DRY
 - Function and variable annotations

### Naming
#### Classes
CamelCase

#### Functions and vars
snake_case

#### Constants
UPPER_CASE_WITH_UNDERSCORES

### Imports
Write `__all__` magic method with objects to be imported in `__init__.py` 

#### Example
```python
from .buttons import InlineKeyboardsButtons

__all__ = [
    "InlineKeyboardsButtons",
]
```