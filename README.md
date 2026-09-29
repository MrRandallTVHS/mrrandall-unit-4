# Task 2: Service and Orchestrator

Complete this task on the `task-2` branch.

## Starter Code

The original combined system is located at:

`starter/monolithic_retail_system.py`

Do not overwrite or replace the starter file. Use it as evidence for your
monolithic-architecture analysis and as a reference for the grocery system's
existing behavior.

## Required Code Files

Select one capability from the starter system:

- Cart
- Inventory
- Payment

In `services/`, create:

1. One service file for the capability you selected:
   - `cart_service.py`, or
   - `inventory_service.py`, or
   - `payment_service.py`
2. `orchestrator_service.py`

The service contracts and recommended function interfaces are provided in
`SERVICE_CONTRACTS.md`. The Python files are the code deliverables that
belong in GitHub.

## Running the Code

Run the orchestrator from the `services/` folder:

```text
python orchestrator_service.py
```

If your system uses `python3`, run:

```text
python3 orchestrator_service.py
```

The orchestrator should call the selected service and display one successful
result and one unsuccessful or invalid result. Web servers, ports, separate
terminals, and HTTP requests are not required.

## Canvas Submission

Use `reference/Test Cases.md` to plan and run the required tests. Record the
test input or action, expected result, actual result, and pass or revision
decision in the Canvas submission workbook. Include the required screenshot
of the test output.

Submit the written architecture responses, service explanation, diagram,
test results, and screenshots through Canvas. Submit the service code and
commit history through your personal GitHub repository as directed in the
task instructions.

## Related Reference Files

- `SERVICE_CONTRACTS.md` explains the service responsibilities and recommended
  function interfaces.
- `services/README.md` explains the required files and how to run the
  orchestrator.
- `../reference/Test Cases.md` provides examples for Cart, Inventory, and
  Payment selections.
