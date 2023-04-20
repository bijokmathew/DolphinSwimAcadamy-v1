# Dolphin Swim Academy

![Dolphin Swim Academy image](readme/)

[View live site]()

This olphin Swim Academy online shopping application built using Django, stripe and allows customer to register and do online shopping. Customer can purchase the swimming costumes as well as reserve swimming classes by using this website. Administrator of the academy can also able to do the product management like add, modify and delete product.Aslo the same action can do for swimming courses. Customers can contact to the academy by using the website.It is the fifth project in the Code institute Full Stack Developer program.

** For testing payment with this site please use the following card details:**

A regular user has been setup with the username of testcustomer1 and password of 2testpassword2

+ When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
For the expiry date, cvc and postal code any series number(s) can be used(once they meet the mimimum values)

## Table of Content

- [Dolphin Swim Academy](#dolphin-swim-academy)
  - [Table of Content](#table-of-content)
- [User Experience](#user-experience)
  - [Strategy](#strategy)
    - [Site Owner Goals](#site-owner-goals)
    - [User Goals](#user-goals)
    - [Target Audience](#target-audience)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [Business Model](#business-model)
  - [SEO](#seo)
  - [Marketing](#marketing)
    - [Facebook Business Page](#facebook-business-page)
  - [Structure](#structure)
    - [Code Structure](#code-structure)
    - [Database](#database)
      - [Physical database model](#physical-database-model)
      - [Models](#models)
        - [User Model](#user-model)
        - [UserProfile Model](#userprofile-model)
        - [Product Model](#product-model)
        - [Category Model](#category-model)
        - [Size Model](#size-model)
        - [Inventory Model](#inventory-model)
        - [Course Model](#course-model)
        - [Contact Model](#contact-model)
  - [Scope](#scope)
      - [**Product Backlog**](#product-backlog)
    - [User stories:](#user-stories)
      - [Error Flow](#error-flow)
  - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)

# User Experience
## Strategy

### Site Owner Goals

The primary goal of the website from the site owners perspective is as follows:
- To enable customers to purchase products listed on the site
- To allow a user to navigate the website and view product details
- To allow a user to create an account & log in to an existing account
- To allow a user to view their order history and account details
- To allow users to view the course and able to reserve the course
- To be able to edit, add and remove products from the site

### User Goals

- The primary goal of the website from a site users perspective is as follows:
- To view products and product details
- To easily search for products
- To filter products based on price, category etc
- To register for an account
- To log into/out of an existing account
- To add a product to bag and purchase order
- To be able to view order history
- To contact the site owner

### Target Audience

- Swimming enthusiasts
- Active people
- People who want to learn swimming
- Qualified swimmers and trainers
  
[Return to Table of Contents](#table-of-content)
  
## User Requirements and Expectations

- An easy navigation system with instant learning.
- Able to navigate the site quickly and easily.
- No broken links.
- Responsive and visually appealing on all devices.
- Ability to view products and complete purchases
- Ability to contact the business

## Business Model

For this project, as the primary goal is to sell products direct to consumers. Add all products with image and detailed descriptions, ability to search and ease to purchase, a product inventory with out of stock visibilty, and restrictions on purchasing more items than in stock.

Alternatively, the business could arrange sale or return from the the supplier or sell driect from supplier stock in the online store and carry physical stock in thier own warehouse.

For the nature of this project, the stock is held pysically in the business.

## SEO

Long tag and short tag keyword were searched for in regards to SEO using Google tools and other online resources. These tags have been used in the main HTML head and throughout the project to name images and within main body text.

![SEO keywords HTML](readme/misc/)

## Marketing

### Facebook Business Page

For marketing the website, it has a link to its own social media page in the footer and that has a recipricol link to the site.

Facebook site can be viewed [here](https://www.facebook.com/). 

![Facebook Screenshot](readme/misc/)
![Facebook Screenshot2](readme/misc/)

[Return to Table of Contents](#table-of-content)

## Structure
### Code Structure

The project is developed with variety of applications, as is constructed using the Django Framework.

App details as follows:

- Home - this app contains landing, hero page information about the academy with quick links to the swimming courses and product page, contact-us and about us via the nav bar.

It contains a footer with links to external sites.

- Products - this app contains the the product listings and detail views, users can add items to a shopping cart, filter for items in categories and search for product. Clicking individual items opens a sub page where users can see detailed product information with add to cart options. The product app has a stock inventory so customers cannot add more quantity to the bag than what is physically in stock. If the items are not available then shows 'Out of stock' to the user.  
    - Admin/Site owner can create, read, update and delete product, course and inventory items.
    - Admin/Site owner can fully manage brands, sizes, categories. Also can add and remove items to inventory.
- Courses - Users can view course listings and details and be redirected to the contact form to get in touch and enquire.
- About - this app contains information relating to the business.
- Contact - this app is for users to be able to submit a message related to specific topics to the site owners and recieve acknowledgment. For users with a profile, when logged in, the form pre-populates profile data to remove friction to the user.
- Profile - Users can choose to save his profile info by selecting the option when checkout the product to purchase. Users can view thier purchase history.
- Bag - User can view, add and remove products that they have added to the bag
- Checkout - Users can use the checkout app to purchase selected items. They can see items in the cart and have the option to save profile information during the checkout process.

To complement the apps there are
- project: Project level files - settings.py for project level settings and urls.py to route the website URLS
- templates: Containing the base.html, allauth(django authentication)
- templates (app level): each app has it's own templates directory for HTML to consider portability and re-use.
- urls (app level): each app has it's own url.py file to consider portability and re-use.
- static: Base css and Javascript files
- manage.py: This file is used to start the site and perform funcions during development
- README.md: Readme documentation
- Procfile: To run the application on Heroku
- Requirements.txt: Containing the project dependencies
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in and listed in .gitignore, and on Heroku in app settings

[Return to Table of Contents](#table-of-content)

### Database
#### Physical database model

Database models contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database 
<br>![Database model](readme/misc/)

#### Models
- The following models were created to represent the database model structure for the website

##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_superuser etc

##### UserProfile Model
- The UserProfile model contains information about the users address. This can be created at the time of checkout. The UserProfile Model contains the following fields: userdefault_phone_number, default_street_address1, default_street_address2,default_town_or_city, default_county, default_postcode, default_country.

##### Product Model
- The Product model contains information about products available within each of the categories
- It contains Category as many to many relationship.
- It contains size as a Many-toMany relationship.
- The model contains the following fields:  name, description, category, size, rating, is_active, price, image, slug.

##### Category Model
- The category model contains the available categories for a product item
- The model contains the following fields: name, friendly_name

##### Size Model
- The Size model contains the sizes available for each product. This is linked to the product model through a custom intermediate model as a many to many relationship.
- It acts as a foreign-key for Inventory model and through to Product
- The model contains the following fields: name, friendly_name

##### Inventory Model
- The Inventory model is a custom intermediate model that between Size Model and Product model as a many to many relationship.  It has an inventory 'units' and 'date_added' as an additional field and self generates a unique SKU on save
- The model contains the following fields: product, size, sku, units, date_added

##### Course Model
- The Course model contains all courses present in th academy. There is a subclass for different stage levels.
- The model contains the following fields: name, friendly_name, description, extra_details, price, duration, level, image and slug

##### Contact Model
- The Contact model contains a collection of data submitted by the user when contacting to the site owner.
- It contains contact options subclass as a with preconfigured choices for the user to select
- The model contains the following fields: subject, full_name, email, phone_number,town_or_city, county, postcode, street_address, country and message.

[Return to Table of Contents](#table-of-content)

## Scope

- The project was developed by using agile methodology. During the design process collect the project requirements and write epics broken down into user stories with well defined acceptance criteria and tasks list. Based on the priority move those user stories in to different project sprint cycle like First cycle, Second cycle and Third Cycle in order to achieve MNP.Once finished the user stories changed the status of specific stories into closed state and if all issues related to the sprint closed then move the sprint cycle also in to closed state. During the development time comming up with an enhancement ideas, create stories and epic for those enhancement ideas and moved in to backlog with priorities.
  
![image of user stories](static/docs/images/)

#### **Product Backlog**
- The product backlog for the project can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestone/1)

    * Project's all user stories on board can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/issues)
    * Project all spring cycle can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestones)
  
 ![image of the product backlog](static/docs/images/)
   
- **First Cycle**
    * The First Cycle milestone can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestone/2)
  
    ![image of the First Cycle board](static/docs/images/)

- **Second Cycle**
    * The Second Cycle milestone can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestone/3)
      ![image of the iteration 2 board](static/docs/images/)

- **Third Cycle**
    * The Third Cycle milestone can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestone/4)
    ![image of the iteration 3 board](static/docs/images/)

- **Fourth Cycle**
    * The fourth Cycle milestone can be found [here](https://github.com/bijokmathew/DolphinSwimAcademy-v1/milestone/5)
    ![image of the iteration 3 board](static/docs/images/)
### User stories:

1. As an unauthenticated user, I want to be able to navigate the website quickly and easily 
2. As an unauthenticated user, I want to have the option to view all products on the site
3. As an unauthenticated user, I want to be able to search the website for specific products
4. As an unauthenticated user, I want to be able to view detailed descriptions and prices of the products
5. As an unauthenticated user, I want to be able to sort the products and view by price and alphabetically
6. As an unauthenticated user, I want to be able to sort and view products by category
7. As an unauthenticated user, I want to be able to add a product to my bag
8. As an unauthenticated user, I want to be able to quickly navigate through product listing pages
9. As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times
10. As an unauthenticated user, I want to be able to navigate back to the products page after viewing product details
11. As an unauthenticated user, I want to be able to view products added to my shopping bag
12. As an unauthenticated user, I want to be able to increase quantities and remove items from my shopping bag
13. As an unauthenticated user, I want to be able to checkout and purchase products
14. As an unauthenticated user, I want to be able to create an account
15. As an unauthenticated user, I want to be able to log in to / sign out of an existing account
16. As an unauthenticated user, I want to be able contact the business
17. As an unauthenticated user, I want to be able to view the business location
18. As an unauthenticated user, I want to be able to browse available courses
19. As an unauthenticated user, I want to be able to view course details and contact for reservation
20. As an authenticated user, I want to be able to view my order history
21. As an authenticated user, I want confirmation that I have signed out of my account
22. As a site owner, I want users to be able to navigate the website quickly and easily
23. As a site owner, I want users to be able to view the business social media
24. As a site owner, I want to be able to update and edit product descriptions, details and prices
25. As a site owner, I want to be able to view and update products 
26. As a site owner, I want to be able to add products
27. As a site owner, I want to be able to delete products
28. As a site owner, I want to be able to manage product inventory
29. As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory
30. As a site owner, I want to make sure that customers can see which products are out of stock
31. As a site owner, I want to be able to view and update the courses listed
32. As a site owner, I want to be able to add a course
33. As a site owner, I want to be able to delete a course
34. As a user, I want to have confirmation that my order has been successful
35. As admin, I want to be able to create batch actions and manipulate all the data tables in one place
36. As a user, I want to be shown messages that my actions have been successful and unsuccessful*

#### Error Flow
1.  As a site owner, I want error pages that enables users to be able to return to valid areas of the site without using browser controls.

## Skeleton

### Wireframes

<details><summary>About Us</summary>
<img src="readme/wireframes/about-us.png">
</details>

<details><summary>All-course</summary>
<img src="readme/wireframes/all-courses.png">
</details>

<details><summary>All-Products</summary>
<img src="readme/wireframes/all-products.png">
</details>

<details><summary>Checkout</summary>
<img src="readme/wireframes/checkout.png">
</details>

<details><summary>Contact Us</summary>
<img src="readme/wireframes/contact-us.png">
</details>

<details><summary>Course Details</summary>
<img src="readme/wireframes/course-details.png">
</details>

<details><summary>Error Page</summary>
<img src="readme/wireframes/error.png">
</details>

<details><summary>Home</summary>
<img src="readme/wireframes/home-page.png">
</details>

<details><summary>Order History</summary>
<img src="readme/wireframes/order-history.png">
</details>

<details><summary>Payment Confirmation</summary>
<img src="readme/wireframes/payment-confirmation.png">
</details>

<details><summary>Product Details</summary>
<img src="readme/wireframes/product-details.png">
</details>

<details><summary>Profile Edit</summary>
<img src="readme/wireframes/profile-edit.png">
</details>

<details><summary>Profile</summary>
<img src="readme/wireframes/profile.png">
</details>

<details><summary>Register</summary>
<img src="readme/wireframes/register.png">
</details>

<details><summary>Cart</summary>
<img src="readme/wireframes/shopping-cart.png">
</details>

<details><summary>Sign-in</summary>
<img src="readme/wireframes/sign-in.png">
</details>

<details><summary>Sign-out</summary>
<img src="readme/wireframes/sign-out.png">
</details>

<details><summary>Manage Categories</summary>
<img src="readme/wireframes/staff-manage-categories.png">
</details>

<details><summary>Manage Brands</summary>
<img src="readme/wireframes/staff-manage-brands.png">
</details>

