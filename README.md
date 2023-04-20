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