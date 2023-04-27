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
    - [Design](#design)
      - [Wireframes](#wireframes)
      - [Colours](#colours)
      - [Typography](#typography)
  - [Features](#features)
    - [Home page](#home-page)
      - [Header and navigation bar](#header-and-navigation-bar)
      - [Search bar](#search-bar)
      - [Image carousel](#image-carousel)
      - [Footer](#footer)
    - [Products](#products)
      - [All products](#all-products)
      - [Product details](#product-details)
      - [Managing product](#managing-product)
      - [Page order](#page-order)
      - [Pagination](#pagination)
      - [Create product](#create-product)
      - [Update product](#update-product)
      - [Deleting a product](#deleting-a-product)
      - [Categories](#categories)
    - [Courses](#courses)
      - [Course list](#course-list)
      - [Course details](#course-details)
      - [Update courses](#update-courses)
      - [Add courses](#add-courses)
      - [Delete courses](#delete-courses)
    - [Log in](#log-in)
    - [Log out](#log-out)
    - [Register](#register)
    - [Profile page](#profile-page)
      - [Profile information](#profile-information)
      - [Order history](#order-history)
    - [Shopping Cart](#shopping-cart)
      - [Shopping cart](#shopping-cart-1)
      - [Checkout](#checkout)
    - [Contact](#contact)
    - [About](#about)
    - [Administration](#administration)
    - [Messages](#messages)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
      - [Python Libraries](#python-libraries)
    - [Frameworks \& Tools](#frameworks--tools)

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

In additions to apps,the following files are included in the projects
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
<br>![Database model](/readme/misc/dolphinacademy_database_schema.png)

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

### Scope

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
15. As an authenticated user, I want to receive an email confirmation to verify my account and confirmation about the registration is successful
16. As an unauthenticated user, I want to be able to log in to / log out of an existing account
17. As an unauthenticated user, I want to be able contact the business
18. As an unauthenticated user, I want to be able to view the business location
19. As an unauthenticated user, I want to be able to browse available courses
20. As an unauthenticated user, I want to be able to view course details and contact for general queries
21. As an authenticated user, I want to be able to view my order history
22. As an authenticated user, I want confirmation that I have signed out of my account
23. As an authenticated user, I want to be able to view and update my personal information in my profile
24. As a site owner, I want users to be able to navigate the website quickly and easily
25. As a site owner, I want users to be able to view the business social media
26. As a site owner, I want to be able to update and edit product descriptions, details and prices
27. As a site owner, I want to be able to view and update products 
28. As a site owner, I want to be able to add products
29. As a site owner, I want to be able to delete products
30. As a site owner, I want to be able to manage product inventory
31. As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory
32. As a site owner, I want to make sure that customers can see which products are out of stock
33. As a site owner, I want to be able to view and update the courses listed
34. As a site owner, I want to be able to add a course
35. As a site owner, I want to be able to delete a course
36. As a user, I want to have confirmation that my order has been successful
37. As admin, I want to be able to create batch actions and manipulate all the data tables in one place
38. As a user, I want to be shown messages that my actions have been successful and unsuccessful
39. As a user, I want to be able to reset my password if I have forgotten it
40. As a user, I want to be see the small details about the business

#### Error Flow
1.  As a site owner, I want error pages that enables users to be able to return to valid areas of the site without using browser controls.

### Design
The aim of the design of the website was to create a clean and modern website, images and themes are used to show business values and create an enticing site that the visitor wants to explore. 
The fonts are bold, clear and modern, with clear headings to enable easy navigation.

#### Wireframes

<details><summary>Home</summary>
<img src="readme/wireframes/home_resp.png">
</details>

<details><summary>About Us</summary>
<img src="readme/wireframes/about_resp.png">
</details>

<details><summary>All-Products</summary>
<img src="readme/wireframes/product_resp.png">
</details>

<details><summary>Product Details</summary>
<img src="readme/wireframes/product_detail_resp.png">
</details>

<details><summary>Shopping Bag</summary>
<img src="readme/wireframes/shopping_bag_resp.png">
</details>

<details><summary>Checkout</summary>
<img src="readme/wireframes/payment_resp.png">
</details>

<details><summary>Payment Confirmation</summary>
<img src="readme/wireframes/confirmation_resp.png">
</details>

<details><summary>Contact Us</summary>
<img src="readme/wireframes/contact_resp.png">
</details>

<details><summary>All-course</summary>
<img src="readme/wireframes/course_resp.png">
</details>

<details><summary>Course Details</summary>
<img src="readme/wireframes/course-details.png">
</details>

<details><summary>Register</summary>
<img src="readme/wireframes/signup_resp.png">
</details>

<details><summary>Sign-in</summary>
<img src="readme/wireframes/signin_resp.png">
</details>

<details><summary>Sign-out</summary>
<img src="readme/wireframes/signout_resp.png">
</details>

<details><summary>Profile</summary>
<img src="readme/wireframes/myprofile_resp.png">
</details>

<details><summary>Product Manage </summary>
<img src="readme/wireframes/product_mgt_resp.png">
</details>

<details><summary>Inventory Manage </summary>
<img src="readme/wireframes/inventory_mgt_resp.png">
</details>

<details><summary>Error Page</summary>
<img src="readme/wireframes/error.png">
</details>

#### Colours
The colour scheme is primarily blues to represent water which matches the business theme. 
#FFFFFF – Titles & subtitles
#FFFFFF - Body text
##315673- Buttons
##5392C2– Button highlight & search bar
#000000 – Image overlay text
insert colour palette image
After choosing a colour scheme I tested a number of palette options to make sure the it met accessibility standards.
<br>![Color](readme/misc/color.png)
<br>![Accessible Color](readme/misc/accessible-color.png)

#### Typography
Poller One is the font uses for the logo, this font is from the Google Fonts.
Urbanist is the font used across all of the headings and text across the website, it has been used in different 
weights and different cases to highlight titles. This font is from the Google Fonts Library.

## Features

The site consists of 11 pages, with the features detailed under each page.

1. Home
2. About
3. Shop
4. Categories
5. Courses
6. Contact
7. Log in
8. Log out
9. Register
10. Prduct Managment
11. Shopping Cart

### Home page
<br>![Home page](readme/features/home-page-nav-bar.png)

The home page consists of the following features:

#### Header and navigation bar
The header contains the logo, products link, categories link, search bar, user account and shopping bag. The header is visible across all pages.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily *

*2 As an unauthenticated user, I want to have the option to view all products on the site.*

*3 As an unauthenticated user, I want to be able to search the website for specific products*

*6 As an unauthenticated user, I want to be able to sort and view products by category*

*9 As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times.*

*11 As an unauthenticated user, I want to be able to view products added to my shopping bag.*

*14 As an unauthenticated user, I want to be able to create an account.*

*16 As an unauthenticated user, I want to be able to log in to / log out of an existing account.*

*24 As a site owner, I want users to be able to navigate the website quickly and easily*

#### Search bar
<br>![Home page](readme/features/search-bar.png)

The search bar is part of the header and this features appears across all pages. This allows the user to easily search products by name.

This feature covers the following user stories:

*3 As an unauthenticated user, I want to be able to search the website for specific products.*

#### Image carousel
<br>![Home page](readme/features/home-page-carousel.png)

The image carousel is the first image the user is presented with, the carousel provides an aesthetic to engage the user through activity, rather than just having static images

This feature covers the following user stories:
*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily*

#### Footer
<br>![Home page](readme/features/footer.png)

The footer appears across all pages, and contains links to direct the user to all main pages – shop, information, account. As well as links to social media pages and the address of the business.

This feature covers the following user stories:

*2 As an unauthenticated user, I want to have the option to view all products on the site*

*14 As an unauthenticated user, I want to be able to create an account*

*16 As an unauthenticated user, I want to be able to log in to / log out of an existing account*

*17 As an unauthenticated user, I want to be able contact the business*

*18 As an unauthenticated user, I want to be able to view the business location*

*25 As a site owner, I want users to be able to view the business social media*


### Products

The product listing menu consists of the following features:

#### All products
<br>![products page](readme/features/all-products-menu.png)
<br>![products page](readme/features/all-products.png)

When the user first selects the shop link, they have an option to view ‘all products’ or select one of the product categories. On selecting the all products page, every product listing appears in an automatic alphabetical order.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily*

*2 As an unauthenticated user, I want to have the option to view all products on the site*

#### Product details
<br>![products page](readme/features/product-details.png)

The user has the option to view details of any product from the product list. From the product detail page customer has an option to add the product to cart for purchase. The product details appear in a new window and gives the user the product name, rating, price, detailed product description, an option to select size and quantity. The user can then add the product to their cart, and either go to the bag or continue shopping.

Before adding the product to cart, always check the selected quantity of the product is available in the stock. 

When an item becomes out of stock, the size selection automatically shows out of stock, and the user will be unable to select this product for purchase.

This feature covers the following user stories:

*4 As an unauthenticated user, I want to be able to view detailed descriptions and prices of the products*

*7 As an unauthenticated user, I want to be able to add a product to my bag*

*10 As an unauthenticated user, I want to be able to navigate back to the products page after viewing product details*

*31 As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory*

*32 As a site owner, I want to make sure that customers can see which products are out of stock*

#### Managing product

When logged in as admin, the admin has the ability to delete or update any product from the product details page or product list page. Admin can edit the title, description, category, size options, price and image. 

This feature covers the following user stories.

*26 As a site owner, I want to be able to update and edit product descriptions, details and prices*
*27 As a site owner, I want to be able to view and update products*
*28 As a site owner, I want to be able to delete products*

#### Page order
<br>![products page](readme/features/product-order.png)

The user has the option to select the order in which to view the products are listed. They can order by price (ascending or descending) or alphabetically (ascending or descending). 

This feature covers the following user stories:

*5 As an unauthenticated user, I want to be able to order the product pages by price, and alphabetically*

#### Pagination
<br>![products page](readme/features/pagination.png)

The pagination appears at the top and bottom of the products page, it shows the user which product page they are on, and gives the user the ability to easily navigate through the product pages.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily *

*10 As an unauthenticated user, I want to be able to quickly navigate through product listing pages*

#### Create product
<br>![products page](readme/features/create-product.png)

The option to create a product appears in the shop dropdown menu when logged in as a admin. It allows admin user to create a new product with blank required fields. 

This feature covers the following user stories:

*28 As a site owner, I want to be able to add products*


#### Update product
<br>![products page](readme/features/update-product.png)

When logged in as a admin, edit option available on product list and product details page, the user has the ability to update the selected item.

This feature covers the following user stories:

*26 As a site owner, I want to be able to update and edit product descriptions, details and prices*
*27 As a site owner, I want to be able to view and update products*

#### Deleting a product
<br>![products page](readme/features/delete-product.png)

When logged in as a admin, delete option available on product list and product details page, the user has the ability to delete the selected item.

This feature covers the following user stories:

*29 As a site owner, I want to be able to delete products*

#### Categories
<br>![products page](readme/features/categories-header.png)
<br>![products page](readme/features/categories-all-products.png)

The category list appears when the user selects the cetegories link in the navbar, as well as on the all products page. The categories allow the user to filter and browse certain products.

This feature covers the following user stories:

*2 As an unauthenticated user, I want to have the option to view all products on the site*
*6 As an unauthenticated user, I want to be able to sort and view products by category*

### Courses

This page consists of the following features:

#### Course list
<br>![courses page](readme/features/course-list.png)
The course link is located in the navbar, and the dropdown menu lists all available courses. Each courses has it's descriptions and an option to view more details or enquire to book.

This feature covers the following user stories:

*17 As an unauthenticated user, I want to be able contact the business*

*19 As an unauthenticated user, I want to be able to browse available courses*

*20 As an unauthenticated user, I want to be able to view course details and request a booking*

*33 As a site owner, I want to be able to view and update the courses listed*

*34 As a site owner, I want to be able to add a course*

*35 As a site owner, I want to be able to delete a course*

#### Course details
<br>![course page](readme/features/course-details.png)

The course details page shows the selected course with a more detailed description, and options to reserve or go back to the previous page.

This feature covers the following user stories:

*17 As an unauthenticated user, I want to be able contact the business*

*19 As an unauthenticated user, I want to be able to browse available courses*

*20 As an unauthenticated user, I want to be able to view course details and request a booking*

#### Update courses
<br>![courses page](readme/features/update-course.png)

When logged in as a admin, edit option available on course details page, update option allows admin to update the course.

This feature covers the following user stories:

*33 As a site owner, I want to be able to view and update the courses listed.*

#### Add courses
<br>![courses page](readme/features/create-course.png)

When logged in as a admin, admin can selects create a course from the dropdown menu in the navbar and admin can add course.

This feature covers the following user stories:

*34 As a site owner, I want to be able to add a course*

#### Delete courses
<br>![courses page](readme/features/delete-course.png)

When logged in as a admin, delete option available on course details page, delete option allows admin to delete the course from the list of course.

This feature covers the following user stories:

*35 As a site owner, I want to be able to delete a course*


### Log in
<br>![login page](readme/features/sign-in.png)

The user can access the log in via the links in the Navbar and footer, they are taken to a log in page that also features a link to create a new account.
A confirmation box appears below the my accout in the Navbar to tell the user they have logged in successfully.

If the user has forgotten their password, there is a link to perform a password reset where an email is sent to the user's requested email address.

This page covers the following user stories:

*16 As an unauthenticated user, I want to be able to log in to / log out of an existing account*

*39 As a user, I want to be able to reset my password if I have forgotten it*

### Log out
<br>![logout page](readme/features/sign-out.png)

The user can access the log out via the links in the Navbar and footer, they are taken to a log out page and confirmation box appears below the my accout in the Navbar to tell the user they have logged out successfully.

This page covers the following user stories:

*16 As an unauthenticated user, I want to be able to log in to / log out of an existing account*

*22 As an authenticated user, I want confirmation that I have signed out of my account*


### Register
<br>![register page](readme/features/sign-up.png)

The register page can be accessed from the Navbar link across all pages. The user is asked to create a username and password for future logins. 
The user gains benefits such as saving shipping details and viewing order history.

This page covers the following user stories:

*14 As an unauthenticated user, I want to be able to create an account*

*15 As an authenticated user, I want to receive an email confirmation to verify my account and confirmation about the registration is successful*


### Profile page

#### Profile information 
<br>![profile page](readme/features/profile-info.png)
<br>![profile page](readme/features/edit-profile.png)

When the user is logged in, they are able to view their profile and purchase history. User can also update their profile info.

This feature covers the following user stories:

*23. As an authenticated user, I want to be able to view and update my personal information in my profile*

#### Order history 
<br>![profile page](readme/features/profile-info.png)
<br>![profile page](readme/features/order-history.png)

When the user is logged in, they are able to view their previous order history. After selecting the order number, user can veiw order in more detail. This page includes order number, product and cost, delivery address and billing information.

The user is then given the option to return to profile.

This page covers the following user stories:

*21 As an authenticated user, I want to be able to view my order history*
*23 As an authenticated user, I want to be able to view and update my personal information in my profile*


### Shopping Cart

The shopping cart is always visible in the Navbar on each page. The quantity is always visible and updates whenever product is added.

#### Shopping cart
<br>![shopping page](readme/features/shopping-cart.png)
<br>![shopping page](readme/features/cart-item-removed.png)

When the user select cart from Navbar and it takes user to car view, user can adjust the quantities of the products by selecting minus to take the quantity to zero removes the item from the bag altogether. The user has confirmation that the product has then been removed.

This feature covers the following user stories:

*9 As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times*

*11 As an unauthenticated user, I want to be able to view products added to my shopping bag*

*12 As an unauthenticated user, I want to be able to increase quantities and remove items from my shopping bag*

#### Checkout
<br>![shopping page](readme/features/checkout.png)

User can go to checkout page by selecting checkout option from bag or from success message of add to bag. Checkout page which displays the items in their bag, quantity and payment details.

When the user is already logged in, payment form is prepopulated with user saved delivery and contact information.

When the user is not logged in, payment form is empty for the user to complete their details and they are given the option to create an account or log in.
<br>![shopping page](readme/features/checkout-unauthenticated.png)

When the card details have been entered correctly a confirmation page is displayed and the order confirmation is sent the to the user’s email address.
<br>![shopping page](readme/features/order-confirmation.png)

This feature covers the following user stories:

*13 As an unauthenticated user, I want to be able to checkout and purchase products*

*36 As a user, I want to have confirmation that my order has been successful*


### Contact
<br>![contact page](readme/features/contact.png)

The contact page contains a contact form for user to complete their details to contact the business. User can go to contact page from Navbar as well as from course enquire option. It features different subject matters for the user to select from which helps the admin can easily deal with customer messages.

This page covers the following user stories:

*17 As an unauthenticated user, I want to be able contact the business*


### About
<br>![about page](readme/features/about-us.png)

The about page features an overview of the business to engage users and help build trust to make them purchase products from the site. User can go to about page from Navbar

This page covers the following user stories:

*40 As a user, I want to be see the small details about the business*


### Administration
<br>![admin page](readme/features/admin-panel.png)

The Django admin panel is a built in tool that enables the admin users to create batch actions and manipulate all the data in tables in one place.

This page covers the following user stories:
*37 As admin, I want to be able to create batch actions and manipulate all the data tables in one place*


### Messages
<br>![admin page](readme/features/success-message.png)

User should get the feedback about his action like success, error, info, warning messages.Feedback messages are shown at below my account in Navbar to confirm the user's action has been applied.
After certain actions, error messages are shown below my account in Navbar to confirm the user's action has been not been applied.

This page covers the following user stories:
*38 As a user, I want to be shown messages that my actions have been successful and unsuccessful*

## Future Features
 add brand
 create category, size managment
 add color option
 add option to purchase for course
 add f/q in about page
## Technologies Used

### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JS ES6](https://en.wikipedia.org/wiki/JavaScript)
- [Django](https://www.djangoproject.com/)
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Markdown](https://www.markdownguide.org/getting-started/)

#### Python Libraries

- asgiref==3.6.0
- crispy-bootstrap5==0.7
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-filter==23.1
- oauthlib==3.2.2
- Pillow==9.4.0
- python3-openid==3.2.0
- pytz==2022.7.1
- requests==2.27.1
- requests-oauthlib==1.3.1
- sqlparse==0.4.3
- stripe==5.2.0

### Frameworks & Tools
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0) - for general site layout, grid, flex, carousel.
- [Bootstrap Icons 1.8](https://getbootstrap.com/) - for various icons in the site
- [Postgres](https://www.postgresql.org/) - the site is deployed on Heroku using a Postgress database.
- [SQLLite](https://www.sqlite.org/index.html) - this database was used in local development.
- [Gitpod](https://gitpod.io/) - IDE of choice for this project.
- [Github](https://github.com/) - used as the code repository.
- [Google Fonts](https://fonts.google.com/) - used for the main body font and some headings.
- [Balsamiq](https://balsamiq.com/) -  used to create the website wireframes.
- [Font Awesome](https://fontawesome.com/) - Font awesome was used to provide the relevant fonts/icons for the website social media icon links.
- [JQuery](https://jquery.com) - JQuery was used in some javascript files for DOM manipulation
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - for validation of the css in the project.
- [HTML Markup Validation Service](https://validator.w3.org/) - for validation the HTML in the project.
- [Firefox dev tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html) - troubleshooting and debugging of the project code.
- [Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) - for performance, accessibility, progressive web apps, SEO analysis of the project code.
- [Responsive Design](http://ami.responsivedesign.is/) - for website mockup.
- [JSHint](https://jshint.com/) - for javascript validation.
- [PEP8](https://www.python.org/dev/peps/pep-0008/) - for python validation.
- [Quick Database diagrams](https://www.quickdatabasediagrams.com)- for the database schema diagram.
- [Facebook](https://www.facebook.com) - for social media marketing
- [Stripe](https://stripe.com/gb) - For payments
- [Amazon Web Services](https://aws.amazon.com/) - For static file hosting
