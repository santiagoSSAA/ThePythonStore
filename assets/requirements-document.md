# Requirements document
By Santiago Sanchez Pulgarin

---

# Action process

### 1. Requirements definition
- Meet the qualifications
- Identify entities.

### 2. Design the Database
- Data model
- Tables structure
- Performance considerations

### 3. API design
- Endpoints
- Data structures
- Security

### 4. FrontEnd design
- User interface
- API integration

### 5. Planning functionalites
- Entities CRUD
- Entities Filters & Search
- Entities Attributes

### 6. Development & implementation
- Data models development
- API implementation
- Frontend Development

### 7. Testing
- Unit tests
- Integration tests
- Usability tests

### 8. Documentation
- Technical documentation
- End-user documentation

---

## Key Characteristics

### Product Catalogue
#### Functional requirements
1. Product Management
- Create Product: Administrators can add new products to the catalog with details such as name, description, price, stock quantity, and category.
- Read Products: Users can view a list of products and access specific details of each product, including name, description, price, stock quantity, and category.
- Update Product: Administrators can edit existing product information such as name, description, price, and stock quantity.
- Delete Product: Administrators can remove products from the catalog.

2. Categories and Attributes
- Manage Categories: Administrators can create, edit, and delete categories to organize products.
- Product Attributes: Administrators can define custom attributes for products, such as size, color, etc.

3. Search and Filters
- Search Products: Users can search for products in the catalog using keywords.
- Filter Products: Users can filter products by category, price range, and other attributes.

4. Cart Interaction
- Add to Cart: Users can add products to the shopping cart from the product detail view.
- Remove from Cart: Users can remove products from the shopping cart.

5. Security and Authentication
- Admin Authentication: Only authenticated users with admin privileges can perform CRUD operations on products and categories.


#### Non-functional requirements

1. Performance
- Response Time: Search, filtering, and accessing product details should be fast and efficient.
- Scalability: The system should be capable of handling an increasing number of products and users without performance degradation.

2. Usability
- Intuitive Interface: The user interface should be easy to use and navigate, allowing users to find products and administrators to manage the catalog efficiently.
- Accessibility: The interface should be accessible to users with different abilities, following best practices for web accessibility.

3. Security
- Data Protection: Catalog data should be protected against unauthorized access and common vulnerabilities.
- Input Validation: All data entered by users and administrators should be validated to prevent SQL injection and other attacks.

4. Maintainability
- Clean and Documented Code: The code should be well-documented and follow best development practices to facilitate maintenance and future improvements.
- Testing: The system should be covered by automated tests to ensure that key functionalities remain operational.

5. Compatibility
- Cross-Browser: The application should work properly on major web browsers.
- Mobile Devices: The interface should be responsive and work well on mobile devices and tablets.

6. Scalability
- Vertical and Horizontal Scalability: The system should be able to scale both vertically (by improving server resources) and horizontally (by adding more servers) to handle larger volumes of data and users.

## Shopping cart
### Functional requirements
1. Add to Cart
- Add Product: Users can add products to their shopping cart from the product detail or product listing page.
- Quantity Management: When adding a product, users can specify the quantity. If the product is already in the cart, the quantity should be updated instead of adding a duplicate item.
- Stock Validation: The system should validate that the requested quantity does not exceed the available stock.

2. View Cart
- Cart Overview: Users can view all the products in their cart, including product details (name, price, quantity, subtotal).
- Price Calculation: The cart should display a real-time calculation of the total cost based on the products and quantities.

3. Update Cart
- Modify Quantities: Users can adjust the quantity of each item directly within the cart.
- Remove Items: Users can remove items from their cart with ease.

4. Checkout Process
- Proceed to Checkout: Users can proceed to a checkout process from the cart page.
- Order Summary: Before placing an order, users should see a summary of the items in the cart, total cost, and any applied discounts or taxes.
- Order Placement: Once confirmed, the cart data is converted into an order and stored in the database. The cart should then be cleared.

5. Persistent Cart
- User-Based Cart Persistence: If a user is logged in, the cart should be persistent between sessions and synchronized across devices.
- Guest Cart: For non-logged-in users, a temporary cart should be maintained via browser cookies or session storage.

6. Cart Notifications
- Visual Feedback: Users should receive visual confirmation when items are added, removed, or updated in the cart.
- Out of Stock Alerts: If a product in the cart becomes out of stock before purchase, users should be notified and prevented from checking out.

7. Integration with Payment and Orders
- Payment Gateway Integration: After confirming the cart, users should be directed to a payment process.
- Order Creation: Upon successful payment, an order should be created, linking the cart items to the user's order history.

### Non-functional requirements
1. Performance
- Real-Time Updates: Adding, updating, and removing items in the cart should happen in real time without requiring a full page reload (AJAX or similar technology).
- Scalable Sessions: The system should handle large numbers of concurrent users with carts in progress, ensuring session data is reliably stored and retrieved.

2. Usability
- User-Friendly Design: The cart interface should be intuitive and easy to interact with. It should provide clear feedback when actions like adding or removing items are performed.
- Responsiveness: The cart should work seamlessly on both desktop and mobile platforms.

3. Security
- Secure Data Handling: Ensure that any cart data (like product prices and quantities) is securely transmitted and validated to prevent tampering.
- Session Hijacking Protection: Implement measures to prevent session hijacking or cart manipulation between users.

4. Reliability
- Consistent Persistence: The cart data should be reliably stored across user sessions, even in cases of unexpected disruptions (e.g., browser crashes).
- Cart Consistency: Ensure that changes made to the cart (like item updates) are reflected immediately and consistently across the application.

5. Scalability
- Distributed Cart Storage: For scalability, consider distributed storage options for cart sessions, especially for guest users. This could be achieved using caching systems like Redis or Memcached.
- Database Efficiency: Ensure that database interactions for cart updates (e.g., adding/removing items, price calculations) are optimized to prevent performance degradation with large numbers of users.

6. Maintainability
- Modular Design: The cart system should be built modularly to allow for easy updates, such as the addition of new payment methods or changes to the checkout process.
- Documentation and Testing: Clear documentation for cart functionality and unit/integration tests to ensure that the cart behaves as expected under various conditions.

7. Cross-Platform Compatibility
- Multiple Devices: The cart should work consistently across different devices and browsers. For logged-in users, the cart should synchronize across their devices.

8. Data Integrity
- Stock Synchronization: The cart should reliably check the availability of products and stock levels at the moment of checkout to avoid issues with overselling.

## Simulated payment process
### Functional requirements
1. Checkout Initialization
- Cart Review: Before initiating the payment, users should review the contents of their cart, including product details, quantity, pricing, taxes, and discounts.
- Address Input: Users should be prompted to enter or select a shipping address (if applicable for a simulated flow).
- Payment Method Selection: Users can choose a simulated payment method (e.g., credit/debit card, bank transfer, or wallet payment).

2. Simulated Payment Gateway
- Payment Simulation: The system will simulate a payment gateway, allowing users to input payment details like card number, expiration date, etc. These should be mock details as no real transactions will occur.
- Successful Payment Flow: Upon submitting the payment form, the system should simulate a successful transaction and move the user to an order confirmation page.
- Failed Payment Flow: Simulate various failed transaction scenarios such as invalid card details, insufficient funds, or network issues, prompting appropriate error messages.

3. Order Creation
- Order Finalization: Once a payment is successfully simulated, the system will create an order in the database, linking the user's cart items, total amount, and other relevant order details (e.g., order status, payment method).
- Receipt Generation: After successful order creation, generate a digital receipt that can be viewed by the user.

4. Order Confirmation
- Confirmation Page: After a successful payment, the user is redirected to an order confirmation page showing the order details, receipt, and estimated delivery information (if applicable).
- Email Confirmation: The system sends an order confirmation email to the user, including a summary of the order and a reference number.

5. Payment Validation
- Simulated Payment Validation: For a more advanced simulation, introduce validation rules (e.g., check card number length, expiration date format) to mimic a real payment gateway experience.
- Retry Payment: If a payment simulation fails, allow the user to retry entering their payment details or change the payment method.

6. Admin Monitoring
- Admin Dashboard: Administrators can view all simulated transactions, including their status (successful, failed) and related order details.
- Order Status Updates: Admins can manually update the order status (e.g., processing, shipped) via the admin panel.

7. Security Checks (Simulated)
- Mock Fraud Detection: Introduce basic mock fraud detection mechanisms that simulate security checks, such as flagging unusually large transactions for further review.

### Non-functional requirements
1. Performance
- Fast Transaction Processing: The payment simulation should happen quickly, providing immediate feedback to the user upon submission of payment details.
- Efficient Handling of Requests: Ensure the system can handle multiple concurrent payment simulations without affecting performance.

2. Usability
- Clear User Flow: The checkout and payment process should be intuitive, guiding users step by step from the cart to payment confirmation.
- Error Handling: Simulated errors (e.g., failed payments) should be presented with clear messages and solutions to guide the user to successfully complete their order.

3. Security
- Secure Mock Payment Forms: Even though it's a simulated payment process, ensure that the form handling follows good security practices, such as using HTTPS, to ensure the user experience is realistic and secure.
- Validation of Input: Simulate real-world security checks, such as basic format validation of credit card numbers and expiry dates.

4. Scalability
- Support for Multiple Payment Methods: Ensure the system is easily extendable to simulate multiple payment methods.
- Load Handling: Ensure that the payment process remains efficient as the number of users grows, simulating high-traffic scenarios effectively.

5. Maintainability
- Modular Design: The payment simulation should be built in a way that allows for future extension, such as adding new payment methods or expanding to support real payments in the future.
- Logging and Monitoring: Implement logging for all payment transactions (even simulated) to allow administrators to track payments and diagnose issues if needed.

6. Reliability
- Transaction Consistency: Ensure that once a payment simulation is processed, the corresponding order and transaction records are accurately created in the database, even under failure conditions.
- Error Recovery: If any part of the simulated payment process fails, the system should be able to recover without affecting the integrity of the order or payment data.

7. Cross-Platform Compatibility
- Mobile Compatibility: The payment simulation should work well on both desktop and mobile browsers.
- Browser Support: Ensure that the simulated payment process is compatible across major web browsers, providing a consistent experience.

8. Testability
- Mock Payment Testing: Provide test cases with predefined card numbers and scenarios that simulate successful and failed payments.
- Unit and Integration Testing: The payment simulation logic should be thoroughly tested to ensure it performs consistently across various situations, including edge cases.

9. Data Integrity
- Accurate Record Keeping: Ensure that order and transaction records are kept consistent and reliable, simulating real-world order tracking and payment reconciliation.
- Simulated Fraud Detection: Introduce mock data checks to simulate fraud detection and payment validation logic, maintaining data integrity even in simulation.

## Admin panel
### Functional requirements
1. User Management
- Admin Authentication: Admins should be able to log in to the admin panel with a secure username and password.
- User Accounts Management: Admins can create, update, and delete user accounts, as well as view user details such as orders, account status, and activity logs.
- Roles and Permissions: Implement role-based access control, where different types of admins (e.g., superadmin, product manager) have access to specific parts of the admin panel.

2. Product Management
- Add/Edit/Delete Products: Admins should be able to create new products, modify existing ones, and delete products from the catalog.
- Stock Management: Admins can update the quantity of products in stock, including adding new inventory or marking products as out of stock.
- Product Categorization: Enable product categorization and allow admins to assign products to different categories and tags for better organization.

3. Order Management
- View Orders: Admins should be able to see a list of all orders placed by users, with details such as user information, order status, and payment details.
- Update Order Status: Allow admins to update the status of orders (e.g., processing, shipped, completed) from the admin panel.
- Refund/Cancel Orders: Enable admins to process refunds and cancel orders, automatically adjusting inventory and order records.

4. Payment Management
- Payment Overview: Admins can review simulated payment details, including successful and failed transactions, and manage user payment information.
- Revenue Tracking: Provide insights and reports into total sales, daily/weekly/monthly revenues, and average order value.

5. Reporting and Analytics
- Sales Reports: Generate detailed reports on sales, product performance, and user behavior (e.g., most popular products, frequent customers).
- Order and Inventory Statistics: Provide insights into inventory levels and order statuses, helping admins monitor the health of the store and prevent stockouts.
- User Activity Tracking: Track user activities, such as login times, order placements, and account changes.

6. Store Configuration
- Settings Management: Admins can configure store-wide settings like tax rates, shipping fees, and promotional offers (discount codes, sales).
- Payment Gateway Configuration: Allow for configuring the simulated payment gateway or integrating real payment gateways in the future.
- Notification Preferences: Configure email notifications for admins and users (e.g., order confirmations, stock updates, payment failures).

7. Security Management
- Audit Logs: Keep detailed audit logs of admin actions, such as product changes, user account modifications, and order status updates.
- Security Settings: Implement options for password management, two-factor authentication (2FA), and session tracking for admins.

8. CMS Features
- Content Management: Admins should be able to update key pages such as the homepage, FAQ, and About Us sections through a simple content management system (CMS) interface.
- Banner and Promotion Management: Admins can create and schedule promotional banners or ads on the site, linking them to relevant products or categories.

9. Customer Support Tools
- Support Requests: Provide a section where admins can view and respond to customer inquiries or issues, including order complaints, return requests, and general questions.
- Refund Handling: Enable an easy process for handling refund requests, including updating order statuses and sending notifications to customers.

### Non-functional requirements

1. Usability
- Intuitive User Interface: The admin panel should be designed with a clean and intuitive user interface that minimizes the learning curve for non-technical users.
- Responsive Design: The admin panel should be fully responsive and mobile-friendly, allowing admins to manage the store from any device.

2. Performance
- Efficient Data Loading: The admin panel should load data quickly, especially for large datasets like product lists, order histories, and reports.
- Scalability: Ensure that the admin panel can handle a growing number of products, users, and orders as the store expands.

3. Security
- Authentication: Implement strong authentication measures such as password encryption, role-based access control, and session management.
- Authorization: Ensure only authorized users can access sensitive sections like user management or payment settings, preventing unauthorized access.
- Protection against Attacks: Implement security practices like CSRF protection, input validation, and rate limiting to protect against attacks like cross-site scripting (XSS) and SQL injection.

4. Reliability
- High Availability: Ensure the admin panel is available 24/7, with minimal downtime or maintenance disruptions.
- Data Integrity: Ensure that any updates or actions taken by admins (e.g., modifying product details, updating orders) are saved correctly and consistently.

5. Maintainability
- Modular Architecture: The admin panel should be built in a modular way, enabling easy updates or addition of new features without disrupting existing functionality.
- Logging and Monitoring: Implement robust logging and monitoring to help track system performance, detect errors, and provide insights into admin usage patterns.

6. Extensibility
- Future Enhancements: Design the admin panel to accommodate future enhancements, such as support for additional payment methods, advanced analytics, or third-party integrations (e.g., shipping providers).

7. Compliance
- Data Privacy: Ensure the admin panel adheres to data privacy regulations like GDPR by implementing features such as data anonymization and opt-in for marketing communications.
- Auditability: Ensure that all actions taken within the admin panel are auditable for legal and compliance purposes, such as tracking user account changes and order status updates.
