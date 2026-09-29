# Business Scenarios

Use Business Scenario 1 as the primary scenario for Task 2. It matches the grocery-system starter code. Business Scenarios 2 and 3 are included as comparison examples that can help you think about different architecture needs.

## Business Scenario 1: Grocery Retail Environment

An e-commerce grocery application is needed to allow customers to browse products, create shopping carts, place orders, and receive groceries through pickup or delivery.

The application must authenticate users and handle product information, inventory, shopping carts, order processing, payment, fulfillment, delivery, and customer notifications.

Demand will be fairly steady but may increase during holidays, severe weather, and major promotional events. The system must continue to respond when many customers shop or place orders at the same time.

The business will change suppliers frequently and may add new products with little notice. Inventory information must be updated as products are received, purchased, substituted, or removed from an order. The business may also change delivery partners based on price and availability.

The system should be easy to maintain, update, test, and redeploy. A change to one part of the system should not require unnecessary changes to every other part. For example, changing the payment provider should not require the inventory system to be rewritten.

When a customer places an order, the system must check inventory, process payment, prepare the order, and arrange pickup or delivery. The customer should receive notifications about important order events.

When selecting an architecture, consider the following questions:

- Which parts of the system have separate responsibilities?
- Which parts may need to change or scale independently?
- How should information move between shopping carts, inventory, payment, fulfillment, and delivery?
- Would the system benefit from independent services, or would a simpler architecture be easier to maintain?
- Would cloud or on-premises deployment better support the business needs?

## Business Scenario 2: Ticketing for Events

A ticketing application is needed to handle seat selection and order processing for a world tour by a popular singer.

Users must be able to authenticate, search for events, view an event, and book tickets.

Traffic will be high, with large spikes whenever a new venue and concert date are announced. Event details must always be available, search results must be returned quickly, and tickets must not be double-booked.

The business needs high reliability and 24-hour availability around the world. Security is very important because the system is expected to be a high-value target for hackers.

## Business Scenario 3: Order Processing

An order processing system must handle order creation, payment, inventory management, and shipping.

Order creation is triggered by the user. When an order is created, the payment system processes the payment. Once payment is processed, the order is fulfilled from inventory. Once the order is fulfilled, it is shipped.

The customer must be notified when the order is created, payment is processed, and the order is shipped.

This scenario is useful for thinking about event-driven architecture because one action causes a sequence of related events. It can also help you compare the communication needs of an order-processing system with the communication needs of the grocery system in Business Scenario 1.
