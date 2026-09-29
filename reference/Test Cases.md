# Test Cases

Use these examples to test the service you selected for Task 2. Your service should be called by `orchestrator_service.py`, and the orchestrator should display an understandable result.

Run one successful test and one unsuccessful or invalid test. Record the action or input, expected result, actual result, and whether each test passed in the Canvas submission workbook.

The exact wording of your output may be different from the examples. The result must clearly communicate whether the operation succeeded or failed.

## Before Testing

1. Confirm that your selected service file is in `task2-microservices/services/`.
2. Confirm that `orchestrator_service.py` calls your selected service.
3. Run the orchestrator from the project folder.
4. Capture the program output for both tests.

## Cart Service Tests

Use these tests if you selected Cart.

### Successful Operation

Start with an empty cart and add two laptops.

Example input:

```python
cart = []
result = add_item(cart, "Laptop", 2)
print(result)
```

Expected result:

- The operation succeeds.
- The cart contains two laptops.
- The result communicates that the item was added.

### Unsuccessful or Invalid Operation

Try to add zero or a negative quantity.

Example input:

```python
cart = []
result = add_item(cart, "Laptop", 0)
print(result)
```

Expected result:

- The operation is rejected.
- The cart is not changed.
- The result communicates that the quantity is invalid.

## Inventory Service Tests

Use these tests if you selected Inventory.

### Successful Operation

Start with five laptops in inventory and add five more.

Example input:

```python
inventory = {"Laptop": 5}
result = update_stock(inventory, "Laptop", 5)
print(result)
print(inventory)
```

Expected result:

- The operation succeeds.
- The inventory contains ten laptops.
- The result communicates that the stock was updated.

### Unsuccessful or Invalid Operation

Try to add zero or a negative quantity.

Example input:

```python
inventory = {"Laptop": 5}
result = update_stock(inventory, "Laptop", -2)
print(result)
print(inventory)
```

Expected result:

- The operation is rejected.
- The inventory is not changed.
- The result communicates that the quantity is invalid.

## Payment Service Tests

Use these tests if you selected Payment.

### Successful Operation

Process a valid payment of 2000 using a supported payment method.

Example input:

```python
result = process_payment(2000, "credit_card")
print(result)
```

Expected result:

- The operation succeeds.
- The result communicates that the payment was processed.
- The result includes the payment amount or another clear confirmation.

### Unsuccessful or Invalid Operation

Try to process a payment with a zero or negative amount.

Example input:

```python
result = process_payment(-2000, "credit_card")
print(result)
```

Expected result:

- The operation is rejected.
- No payment is processed.
- The result communicates that the amount is invalid.

## Orchestrator Requirement

The orchestrator must call the function in your selected service and display the result. It should not duplicate the selected service's business logic.

For each test, the output should make clear:

- Which operation was attempted
- Whether the operation succeeded or failed
- What result was returned by the selected service

If your selected service uses different but clearly documented function names or parameter names, use the interface provided in `SERVICE_CONTRACTS.md` and explain the difference in your Canvas submission.
