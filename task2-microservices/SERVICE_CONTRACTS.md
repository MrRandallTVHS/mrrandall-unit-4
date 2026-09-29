# Service Contracts

These contracts define the minimum behavior expected for Task 2. Students
select one service to implement and create an orchestrator that calls that
service. The implementation may use functions, classes, dictionaries, lists,
or another reasonable Python design, but the service must have a clear
interface and return an understandable result.

This version of the task uses local Python modules. Students do not need to
create web servers, use ports, or implement HTTP endpoints.

## General Service Requirements

The selected service must:

- Be saved in `task2-microservices/services/`.
- Provide one clear operation that the orchestrator can call.
- Validate important input, such as zero or negative quantities or amounts.
- Return a result that clearly communicates success or failure.
- Keep its own business logic separate from the orchestrator.

The function names below are recommended interfaces. Students may use the
same names and parameters or make a small, clearly explained adjustment.

## Cart Service

Recommended function:

```python
add_item(cart, item, quantity)
```

The function should add the requested item and quantity to the cart.

Expected behavior:

- A positive quantity adds the item to the cart and returns a success result.
- A zero or negative quantity is rejected and returns an error result.
- The function should not directly process payment or manage inventory.

Example input:

```python
cart = []
result = add_item(cart, "Laptop", 2)
```

## Inventory Service

Recommended function:

```python
update_stock(inventory, item, quantity)
```

The function should add the requested quantity to the selected item's stock.

Expected behavior:

- If `inventory` begins with `{"Laptop": 5}`, adding `5` results in a stock
  total of `10`.
- A positive quantity updates the inventory and returns a success result.
- A zero or negative quantity is rejected and leaves the inventory unchanged.

Example input:

```python
inventory = {"Laptop": 5}
result = update_stock(inventory, "Laptop", 5)
```

## Payment Service

Recommended function:

```python
process_payment(amount, method)
```

The function should process a payment using the supplied amount and payment
method.

Expected behavior:

- A positive amount and recognized payment method return a success result.
- A zero or negative amount is rejected.
- The result clearly communicates whether payment was processed.

Example input:

```python
result = process_payment(2000, "credit_card")
```

## Orchestrator

The file `orchestrator_service.py` should coordinate the selected service.
It should:

- Import or otherwise call the selected service operation.
- Provide input for the operation.
- Display or return the service result in an understandable form.
- Allow both a successful and an unsuccessful or invalid test.
- Keep coordination separate from the selected service's business logic.

The orchestrator should not copy all of the service's business rules into its
own code. For example, if the student selects Inventory, the inventory
validation and stock update should remain in the inventory service. The
orchestrator should call the inventory function and display its result.

## Required Testing

Students must run the selected service through the orchestrator and record:

1. One successful operation.
2. One unsuccessful or invalid operation.

Use the matching examples in `reference/Test Cases.md`. The exact wording of
the program output may vary, but the result must make the outcome clear.
