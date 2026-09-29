# Task 2 Services

For Task 2, select **one** capability from the grocery system and create a
small Python service for that capability. Then create an orchestrator that
calls your service.

You do not need to create all three services. Choose one:

- Cart
- Inventory
- Payment

## Required Files

Create these two files in this folder:

1. The service file for the capability you selected:
   - `cart_service.py`, or
   - `inventory_service.py`, or
   - `payment_service.py`
2. `orchestrator_service.py`

Your completed folder should look similar to one of these examples:

```text
services/
|--cart_service.py
|== orchestrator_service.py
```

or:

```text
services/
|-- inventory_service.py
|-- orchestrator_service.py
```

or:

```text
services/
|-- payment_service.py
|-- orchestrator_service.py
```

## Service File

The selected service file should:

- Have one clear responsibility.
- Provide the operation described in `SERVICE_CONTRACTS.md`.
- Validate important input.
- Return or display an understandable success or error result.
- Keep its business rules inside the service rather than inside the
  orchestrator.
- Include comments explaining important design decisions.

Use the matching examples in `reference/Test Cases.md` to plan your
successful and invalid tests.

## Orchestrator File

`orchestrator_service.py` should:

- Import or call the service you selected.
- Provide test input to the service.
- Display the service result.
- Include one successful test and one unsuccessful or invalid test.
- Coordinate the operation without copying the service's business logic.

Run the orchestrator from this folder with:

```text
python orchestrator_service.py
```

If your system uses `python3` instead of `python`, use:

```text
python3 orchestrator_service.py
```

The exact output wording is your choice, but the output must make it clear
which operation was attempted and whether it succeeded or failed.
