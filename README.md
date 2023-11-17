![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

...............................................
# [Snap Call Coaching](https://snapcallcoaching-146b3f7fc4be.herokuapp.com/)

<image>

[Snap Call Coaching](https://snapcallcoaching-146b3f7fc4be.herokuapp.com/) is a website which sells online poker coaching services. It is aimed at all levels of players from absolute beginner right through to aspiring proffesionals. 


## Table of content

- [User Experience](#user-experience)
  - [Goal](#goal) 
  - [Design](#design)
  - [User Stories](#user-stories)
  - [Features](#features)

- [Marketing](#marketing)
  - [SEO](#seo) 
  - [Social Media](#social-media)
  - [Newsletter Signup](#newsletter-signup)

- [Functionality](#features)
  - [CRUD](#crud)
  - [Database & Models](#database-&-models)
    
- [Validation](#validation)
  
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
  - [Features to be Implemented](#features-to-be-implemented)
  
- [Libraries and Tools](#libraries-and-tools)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
  


## User Experience


### Goal 
The goal of the website is to sell online poker coaching courses to all level of players. Courses range from absolute beginner right through to aspiring proffessionals. Price ranges for the courses reflect the level of expertise covered. 

#### Business Plan
The site follows a Business to Consumer model. All of its services/products are online. The site sells online courses for a once off payment and some of the more advanced courses include one-on-one coaching sessions as part of the package.

##### In designing the site these content questions were considered and answered as follows:

- What do  users need?
  - To learn how to play poker
    - Rules of the game
    - Basic strategy / fundamentals
    - Pre-flop charts
    - Bankroll management
  - To learn intermediate strategy
    - 3-bet ranges
    - Post flop strategy & hand reading
    - Tournament strategy vs cash game
    - How to beat small stakes / micro stakes
    - Dealing with downswings
    - Leak finder
  - Advanced / professional strategy
    - Using heads up displays
    - Calculating equity
    - Using solvers
    -  Poker math and game theory
    - Deep stack strategy
      
- What information and features can we provide to meet those needs?
  - Courses containing the information required. These courses will include;
    - Beginners
      - Pre-flop charts
      - Instructional videos
      - Quizzes
    - Intermediate
      - Range charts
      - Videos giving detailed breakdown of strategy
      - Users can submit hand histories for review by a pro
    - Advanced
      - All of the above plus live one on one coaching from a pro
        
- How can we make the information easy to understand?
  - Courses will be made available at Beginner, intermediate and advance level. This will be clearly set out and language used will be tailored to suit the target demographic of each course.
    
- How can we demonstrate expertise, authoritativeness and trustworthiness in our content?  
  - The site will contain profiles of the coaches who will all be professional poker players. Coach bios will list their experience and accoaldes. This will give them the authority and expertise to teach.
  
- Would there be other pages within the site which we could link to from a chosen page?
  - Each course will list the coaches available and contain links to each coaches profile. Each coaches bio will list the the course they coach on and link to those courses. 

##### In determining the marketing of the site these questions were considered and answered:

- Who are our users?
  - Given the profile of poker poker players in general our users are likely to be mostly males between the ages of 18 - 45
    
- Which online platforms would we find lots of our users?
  - Many of our users would be frequent users of the larger poker playing sites such as PokerStars, GGPoker and 888Poker. They will also browse online forums such as twoplustwo and r/poker on reddit. 
  
- Would our users use social media? If yes, which platforms do you think you would find them on?
  - Typically our users would use YouTube to view poker content as well      as a smaller markety on instagram and tiktok.

- What do our users need? Could we meet that need with useful content? If yes, how could we best deliver that content to them?
  - Yes, our users would be looking to learn better poker skills. This can be provided via our online training courses.
    
- Would our business run sales or offer discounts? How do you think your users would most like to hear about these offers?
  - Looking at other similar business models, we will offer a newsletter that provides poker tips and strategies for free. Users can subscribe to this newsletter via email. These emails can also be used to offer discounts and promote newly added courses to our user        base.
    
- What are the goals of our business? Which marketing strategies would offer the best ways to meet those goals?
  -  The goal of the business is to sell our courses. The best marketing strategy for this starting out (for budget reasons) would be free/ low cost. It is intended to use our newsletter service as a means of promotion. Once we have a bigger user base and more budget       it is intended to market our site on the various poker forums and poker videos appearing on YouTube.
  -  As the site grows it maybe possibel to approach popular proffessional players with whom we can pay to promote our courses on their social media.
  -  Additionally, we will include a feature where users who have purchased a course can leave a testimonial as to their experience with the content. This will serve        as a reasurance to prospective purchasers that we profide high quality content. 



### Design
The website was designed with simplicity in mind. There is minimal clutter with the focus being on the courses themselves. The font [Kanit](https://fonts.google.com/specimen/Kanit) was chosen as it adds to the minimalist feel of the site while also haveing a computational / mathematical theme which compliments our course content. [It is a combination of concepts, mixing a Humanist Sans Serif motif with the curves of Capsulated Geometric styles that makes it suitable for various uses, contemporary and futuristic](https://fonts.google.com/specimen/Kanit/about). For the color design, Green was chosen as it is reflective of the green felt of a poker table. The greys and blacks compliment the dark green color and were taken from palettes available on [Color Space](https://mycolor.space/). The logo was designed using [Logo.com](https://logo.com/).

### User Stories
Agile methodoligies were used to plan and design the website. User stories were created using issues on GitHub and were added  to five epics (milestones):
- Epic 1: Landing Page
- Epic 2: Courses
- Epic 3: Coaches
- Epic 4: Marketing
- Epic 5: Additional Functionality
  

<image>

These epics were broken down into user stories which were labeled and categorised in accordance with MoSCoW principles. 
The progress of these user stories were traked via the use of the GitHub kanban-board. 

<image>

While the use of agile methodologies was useful in staying on track with the project, on reflections some of the user stories should have been broken down into smaller user stories to make them more manageable.


#### Must Haves (Completed)
- As a **user** I can **view available courses** so that **choose which course suits me best**.
- As a **site owner** I can **provide a function where users can sign up for weekly emails** so that **I have a database of customers to whom I can make offers**.
- As a **user** I can **use a nav bar** so that **easily navigate to different sections of the site**.
- As a **user** I can **view details and bio of all coaches** so that **i can be assured of the quality of the courses**.
- As a **admin** I can **CRUD courses on the front end** so that **I can easily update the site with new courses as they become available**.
- As a **site owner** I have **a facebook business page** so that **I can market the business**.
- As a **user** I can **create an account** so that **I can access materials purchased**.
- As a **developer** I have **included key words throughout the site's code** so that **the site will rank highly on search engines**.
- As a **user** I can **purchase a course** so that **I can access the course materials**.
- As a **user** I can **see a 404 page when there is an error** so that **the site feels fully functional**.
- As a **user** I can **receive messages throughout the site** so that **i know what actions i have taken**.

#### Should Haves (completed)
- As a **user** I can **see a clear description of the site and what it offers** so that **I can immediately know if I am interested in what the site offers**.
- As a **user** I can **view which coaches teach on which course** so that **I can know who will be teaching each course**.
- As a **user** I can **click a course in a coaches bio** so that **I can be brought to a page to purchase that course**.
- As a **user** I can **add items to a shopping cart** so that **i can purchase multiple courses at once**.

#### Could Haves (completed)
- As a **user** I can **add a testimonial** so that **users can see how other users feel about a course**.
- As a **user** I can **view images of each coach** so that **I can easily identify each coach**.
- As a **user** I can **click a coaches name when viewing a course** so that **i can view the coaches bio**.

##### Won't Haves and Not Completed
- As a **admin** I can **create blog posts** so that **i can give site users tips on playing poker and content can be used for marketing purposes**. (Could Have)
- As a **user** I can **view testimonials from the homepage** so that **I can immediately see what past users thought of the site**. (Won't Have)
- As a **site owner** I can **display books that are for sale** so that **I can sell books to users**. (Won't Have)


### Features
- #### Navbar
	The Navbar contains our logo created using [Logo.com](https://logo.com/). This and the whole navbar appears on every page of the site. 
	
	The navbar contains links to other pages including:
	- Home (to bring the user back to the homepage from anywhere on the site.
	- Courses (for a list of all courses available for purchase)
	- Our Team (for a view of all of our poker coaches and their bios)
	- Register and Login (if the user is not authenticated)
	- Logout (if the user is authenticated)

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/17cd9edf-3ad3-4aec-bb85-cf8ff086a5d3)
  
	- My Account icon - contains a drop down menu with:
		- Register / Login if user is not authenticated
	 	- My Profile / logout if user is authenticated
	  	- Course Management if user is an admin
	 - Cart icon - states cart empty or displays a number representing the number of items in the cart

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/38ccae4f-2b3b-4cc9-93d9-e6ac011176c4)

	Each link in the navbar will be highlighted if it represents the page that the user is on.

	On smaller devices the navbar collapses into a burger icon but all features arer still available.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/f01a132e-6c03-4f05-b0ee-bc441b862fa4)

- #### Callout
	At the top of each page there is a callout which using template literals is customizable for each page it displays on.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/1de441a9-d0cd-402b-bae8-10a8f704e614)

- #### Landing Page

	The Landing page displays a description of the site and what it offers followed by a link to view our courses. There is also a pokertips signup form provided by [Mail Chimp](https://mailchimp.com/).

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/8ff66f51-57d3-4598-bad0-62a62db29f4c)

	The landing page is responsive and the elements will stack on top of one another for mobile views.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/41aec488-146a-43f0-9b29-db5f905048c6)

- #### Footer
	The footer also appears on all pages of the site. It contains a link to our Facebook Business Page as well as a link to our Privacy Policy generated by [Privacy Policy Generator](https://www.privacypolicygenerator.info/).

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/9318b597-de90-4af1-a339-a2c937e05815)
	
	Privacy Policy.
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/0727c9de-a451-49b9-bc6b-b6c10decbb53)


- #### Courses
	The Courses page displays all of the courses that have been uploaded by the site admin. Each post displays the course name, a brief description, a (customizable) background image and a View Course Contents button:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/61c66787-cbf9-487f-8de3-2a7f2937f10e)
	
	This is also responsive for mobile devices:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/5a9cf234-d4dd-4b9c-b18e-c82b8a2020fd)
	
	Where the user is a site admin, buttons will also display the options to edit or delete the coourse:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/f4dc26dd-f7ad-4cba-81db-9f8f6ed8280e)


- #### Course Detail
	The Course Detail page displays the content of each course taken from the COURSE Model. There is the name, brief description, a longer detailed description of the contents and links to the coaches for that course. There are also two buttons, one to return the other courses and one to purchase the course which when clicked automatically adds the course to the users cart and redirects the user to the cart page. A pop up message will also disply saying the course has been added to the cart.
	
	<image>
	
	Mobile View:
	
	<image>
	
	If a user has purchased a course then there is an option to add a testimonial of their experience on the course. Once submitted via the TESTIMONIALS Model, this needs to be approvewd by a site admin after which it will appear on the other side of the screen. Once a user has submitted a testimonial the option to submit one no longer appears.
	
	<image>
	
	If the user is a site admin then buttons to edit or delete the course also display here. If the user has already purchased this course then the purchase now button is removed and instead they see the following option:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/bc54ef7b-ebf4-4bb2-95fd-44916af0b5c4)
	

- #### Our Team
	The Our Team page displays all of the coaches that are currently providing their servicves taken from the COACH Model. Each post displays the name and biography of the coach along with a profile picture and a list of their accolades. The courses they are coaching on are also linked. New coaches can be added by site admins via the admin panel.
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/3ee3bbb5-7247-4ffb-9101-df611b48c982)
	
	Mobile view:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/20563da9-a9a2-4016-ba91-8bacaa6ec6d1)


- #### Shopping Cart
	The shopping Cart will display any courses that have been added. The total cost is also calculated and displayed at the end. It is possible to remove courses from the cart by clicking the red X. This will also recalculate the total cost. The user can click "Back to Courses" button incase they want to add additional courses. If an item is in the cart and a user clicks purchase now they are redirected to the cart and a popup message appears stating that the course is already in the cart. Once the user clicks "Secure Checkout" they are taken to the checkout page.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/abd011f4-e6e1-4df7-8b1c-4228f627db33)

- #### Checkout
	At checkout on the left hand side are the billing details to be completed. There are no shipping details as our products/services are entirely online. After filling in the billing details the user is offered the option of signing in or creating an account in order to save the billing details to their profile should they want to make future purchases. If the user is already signed in then they can check a box to automatically save their details to their profile. On the right handside is a brief order summary and order total. Finally the payment details are to be filled in and payments are handled via [Stripe](https://stripe.com/ie).

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/f1a3736a-6b23-4f68-9734-ee56071e4111)

	Once the user clicks complete order a loading overlay will display before redirecting to the Order Confirmation page.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/3018ae9d-a521-4c7f-ac59-7883b16998ca)

- #### Checkout Success
	Once the order is complete a success message displays and the user is redirected to an Checkout Success Page which lists the details of their order.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/55dc8bd7-78c8-40e5-b4fc-838d5dcbb6dc)

	The Checkout Success Page also outlines that a confirmation and details of how to access the course have been sent to their email. 

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/fd9dec23-f59a-4bb9-a313-676331354587)

- #### Register
	Users who wish to register can do so by clicking the link in the navbar or on the dropdown menu of the My Account icon. Once they do so they are taken to the Sign Up page where they are asked to register their details. Once submitted, the user is prompted to check their email for a verification email where they can click a link to confimr this is a valid email address.
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/9cf1f33b-1b63-4304-8642-abea0286b8d3)
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/957f9e54-8238-40ab-b6d6-642e0a3c7f88)
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/8406e4fa-1e60-4c17-b643-47e7340978d6)
	
	The user is then redirected to the Sign In page and a message displays confirming they have verified their email.

- #### Login
	Users are taken to the Sign In page by clicking Login in the navbar or the dropdown menu of the My Account icon. Once on the Sign In Page they can enter their credentials. There is the option to select "Remember me" and also the possibility to reset password if it is forgotten. Once the user signs in they are redirected to the landing page and a message appears stating that they are successfully signed in.
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/68249ab7-7703-4a6d-ab71-163d64d5a249)

- #### Logout 
	A logged in user can logout by clicking logout in the navbar or on the dropdown menu of the My Account icon. They are then taken to the Sign Out page where they can confirm they wish to sign out. Once a user signs out they are redirected to the landing page and a message appears stating they have signed out.
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/59283ac2-40d1-42fd-bcb0-76fffba6dd74)

- #### My Profile
	A user can view their profile by clicking My Profile in the My Account dropdown menu. On the My Profile page they can see their saved billing details, they can update their saved billing details and view the courses they have purchased.
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/c84d4589-6e1d-4d3d-b3e3-bb4df1ab4197)

- #### Edit Course
	An admin can click the Edit Course button from the Courses page or the Course Detail page. They will then be taken to the course edit page and an alert will popup letting them know which course they are editing. Here the admin can edit the details of a course, add further content or change the background image. Once the admin clicks Edit, they are redirected to the course detail page of the course they were editing and a message popsup saying that the course was successfully edited.

	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/3a6f5639-7f4d-4539-bf66-eb7377fd075e)

- #### Delete Course
	If an admin wished to delete a course entirely they can do so by clicking the Delete Course button from the Courses page or the Course Detail page. Once they do so they are redirected to a confirmation page where they are asked to confirm they really want to delete the course. If they choose to delete the course they will be redirected to the Courses page and a message will popup that they have successfully deleted the course.

	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/4b7bb1b3-0d91-4e84-9ecb-39a9f5670264)

- #### Course Management
	Admin users can access the Course Management page from the dropdown menu on the My Account icon. Once on the Course Management page admins can upload a new course using the COURSE Model. Once the new course is added the admin user is redirected t othe course detail view of that course and a message popsup saying course was successfully added.

	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/bb79dea5-6109-468e-bd5a-ffa9004e957c)





#### Messages
The site is equipped with messages throughout to guide the user at all stages of their experience. Examples are below:

<img width="196" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/56369f38-a815-4dfe-b52e-3299f7bbe87f">

<img width="284" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/13b0b5a2-6ddf-418d-9849-edaa6e533a0d">

<img width="209" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/94d84dc4-55d6-4a27-93b8-8699b288d2ca">

#### 404 Page
The site has a custom 404 page that displays is the user lands on a page that does not exist. This includes a button to return home.

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e297f979-f79d-40d8-8ef0-0004f18b383c)


## MARKETING

### SEO
#### Keywords
As part of SEO optimisation we conducted keyword research. This involved brainstorming as many short-tail and long-tail keywords as possible. As part of this process we searched google for our key woords and took note of the autocomplete options as well as the "People also ask" and "Related searches" sections. After compiling our list we then used [Word Tracker](https://www.wordtracker.com/) to find which of our keywords have high volume and low competition. Some of the results are set out below:

![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/9b415325-c1f7-4ba7-8a4d-d0deccf11265)

![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/97a7d21d-ee0f-4306-beab-6d07299c7b97)

![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/06f3ce86-aa94-49c3-857d-d0269ace087b)


Based on the results we selected the keywords highlighted in yellow below:

![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/672a95c8-3017-4242-be06-27c069b8b9a4)

##### HTML Implementation
We included these keywords where appropriate throughout our HTML including:
- using strong and emp tags where applicable
- using rel="noopener" for social media links
- using keywords in our image alt attributes where appropriate
- using keywords in image file names
- adding keywords to the <title>
- adding meta descriptions and keywords sections
  
#### Other
We also incldued in the final site a robots.txt and a sitemap.xml file for further SEO.


### Social Media
As part of our marketing we created a Facebook Business Page. It is hoped that in the future our blogposts can be promoted here as well as discounts or sales. This has been incldued in the footer on all pages of the site.

![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/d6f49bac-85bb-41ca-b8b2-9433a23b786e)


### Newsletter Signup
Similar to other businesses in this market we have implmented a sign up form on our homepage. This was done using [Mail Chimp](https://mailchimp.com/). This offers users the ability to sign up to our newsletter which will be sent weekly. The newsletter will offer free poker tips and strategy to all that sign up. It is hoped that this sign up form will allow us to build a strong userbase of dedicated poker players. The goal is to then use these newsletters to promote discounts or sales that are occuring on the site in the hope of increasing our sales.




## Functionality
### CRUD
#### Create
Users can add a coffee shop to the site. This is done via the use of a crispy form. They also have the option to add comments to a post which also uses crispy forms. Once this is done the post or comment requires approval from the administrator. This is to ensure the quality of the content that is posted to the site.

#### Read
Once a post is made it can be viewed on the homepage and if clicked into it can be seen in more detail. Here any comments that have been added can also be viewed.

#### Update
Users have the option of editing their own posts if they wish. Once a post is updated it requires approval once again. The reasoning for this is to prevent a user's post being approved and then them being able to edit it to say something which is not keeping inline with the sites ethos. 

#### Delete
Users have the option to delete their own posts. If they choose to do so a modal will appear asking them to confirm the deletion. This is to ensure a post is not deleted accidentally as deleting a post cannot be undone and all associated comments will also be deleted.

## DATABASE & MODELS

The below database schema was designed using [DrawSQL](https://drawsql.app/). This was of assistance in visualising the layout of the models to be used.

<img width="556" alt="image" src="https://github.com/tomkelly111/trialworkspace/assets/111172617/6b6984e6-0371-49d8-9f79-661cd3bfde0b">


## TESTING

### Validation

HTML - No errors were returned when code was checked with the official [W3C validator](https://validator.w3.org/), save for:
- On Coach Bios and Course Details page there are "No p elements in scope but a p end tag is seen" errors - i believe this is not correct and has been picked up because of the markdown being provided by django Summernote.


CSS - No errors were returned when code was checked with the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/).


JAVASCRIPT - No errors were returned when code was checked with the official [JS Hint validator](https://jshint.com/).


PYTHON - No errors were shown when code was checked with the Code Institute Python Linter (https://pep8ci.herokuapp.com/) save for 2 errors in settings.py where lines were too long.


Accessibility - I confirmed the code used is accessible by using lighthouse in devtools.

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/01264a54-18ba-4e4c-bcb7-4e8885249d30)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/eb00dac5-2ab8-433e-9f1a-dcfcba18e3a8)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/067b018d-e7cb-431e-8ff2-9e8a3663c775)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e55cd2df-c975-4d81-ba06-786736b6de69)





### Manual Testing
| Page                 | Action                                      | Expected Result                                 | Pass/Fail | Comments                               | Corrected and Retested Result |
| -------------------- | ------------------------------------------- | ----------------------------------------------- | --------- | -------------------------------------- | ----------------------------- |
| **Homepage**         |                                             |                                                 |           |                                        |                               |
|                      | Click on View Our Courses Button             | Redirection to Courses page                      | Pass      |                                        |                               |
|                      | Enter Email to sign up for newsletter        | User is subscribed via Mailchimp                | Fail      | 					    |                               |
|                      | Click Courses in Navbar                      | Redirection to Coaches Bios page                | Pass      |                                        |                               |
|                      | Click Our Team in Navbar                     | Redirection to Coaches Bios page                | Pass      |                                        |                               |
|                      | Click View Our Privacy Policy                | Privacy Policy opens in a new tab               | Fail      | Policy opens in the same tab            | Fixed		     |
|                      | Click Facebook icon                          | Facebook business page opens in a new tab      | Pass      |                                        |                               |
|                      | Click My Account icon when not logged in     | Register/login options display                 | Pass      |                                        |                               |
|                      | Click My Account icon when logged in         | My Profile/logout options display               | Pass      |                                        |                               |
|                      | Click My Profile when logged in              | My profile page displays                        | Pass      | Font color does not match site theme   | Fixed                              |
|                      | Click Cart icon                              | User brought to cart or empty cart option displays | Pass   |                                        |                               |
| **Courses Page**      |                                             |                                                 |           |                                        |                               |
|                      | Click on View Course Content                 | Redirection to Courses detail page               | Pass      | Student Testimonial header displays even when there are no testimonials to display | Fixed |
| **Our Team Page**     |                                             |                                                 |           |                                        |                               |
|                      | Click on course in coach bio                 | Redirection to relevant course                  | Pass      |                                        |                               |
| **Course Detail Page**|                                             |                                                 |           |                                        |                               |
|                      | Click on purchase now button                 | Redirection to cart and course is added to cart | Pass      |                                        |                               |
|                      | Navigate to another course and click purchase now button | Redirection to cart and second course is added to cart | Pass |                                  |                               |
|                      | Try to add a course that is already in cart | Redirection to cart and message states course is already in cart | Pass |                                   |                               |
|                      | Click on back to courses button              | Redirection to Courses Page                     | Pass      |                                        |                               |
| **Shopping Cart**     |                                             |                                                 |           |                                        |                               |
|                      | View shopping cart                           | Total cost is calculated correctly              | Pass      |                                        |                             |
|                      | Click Remove from cart button                | Course is deleted from cart and total is recalculated | Pass |                                  |                               |
|                      | Remove all courses from cart                 | Your cart is empty page displays                | Pass      |                                        |                               |
|                      | Click on secure checkout button              | Redirection to Checkout Page                    | Pass      |                                        |                               |
| **Checkout Page**     |                                             |                                                 |           |                                        |                               |
|                      | Click complete order button without all details filled in | Page refreshes and requests field to be filled in | Pass |                                  |                               |
|                      | Click complete order button with details completed | Redirect to Checkout Success page and user gets confirmation email | Pass |                             |                               |
|                      | Click create an account to save details      | User is brought to sign-up page                 | Pass      |                                        |                               |
|                      | Click login to save details                  | User is brought to sign-in page                 | Pass      |                                        |                               |
| **Purchase course for logged in user** |                                   |                                                 |           |                                        |                               |
|                      | Select to save billing details to profile    | Details are saved to profile                    | Pass      | BUG - details are saved with brackets and quotes surrounding | Fixed           |
|                      | View course already purchased                | Purchase button is hidden and button saying course already purchased displays | Pass |                            |                               |
|                      | View course already purchased                | User has opportunity to add a testimonial      | Pass      |                                        |                               |
|                      | Purchase course                              | Course is added to My Courses in My Profile    | Pass      |                                        |                               |
| **User leaves testimonial** |                                      |                                                 |           |                                        |                               |
|                      | Submit testimonial                           | Message appears saying testimonial is awaiting approval | Pass |                              |                               |
|                      | Submit testimonial                           | Testimonial form no longer appears on course  | Pass      |                                        |                               |
|                      | View course already purchased                | User has opportunity to add a testimonial      | Pass      |                                        |                               |
| **My Profile page**   |                                             |                                                 |           |                                        |                               |
|                      | Update details and click update billing details button | Details are updated and confirmation message appears | Pass |                           |                               |
|                      | Click My Courses button                      | Purchased courses and view other courses option displays | Pass |                             |                               |
|                      | Non-logged in user enters profile URL        | User is brought to sign-in page                | Pass      |                                        |                               |
| **Register Page**     |                                             |                                                 |           |                                        |                               |
|                      | Enter non-matching emails                    | Form does not submit and user is asked to correct | Pass |                                  |                               |
|                      | Enter non-matching passwords                 | Form does not submit and user is asked to correct | Pass |                                  |                               |
|                      | Correctly complete details                   | User receives verification email               | Pass      |                                        |                               |
|                      | Try to login without verifying email         | User is brought to page asking them to verify email | Pass |                              |                               |
|                      | Click email verification button              | User is registered and able to login successfully | Pass |                               |                               |
| **Login Page**        |                                             |                                                 |           |                                        |                               |
|                      | Enter incorrect username or password        | Form does not submit and user is notified of issue | Pass |                                  |                               |
|                      | Click forgot password                        | User is asked to enter email to reset password | Pass |                                  |                               |
|                      | Submit email to reset password               | Page displays saying that email has been sent and user receives email | Pass |                  |                               |
|                      | Click reset password link from email         | User has option to change password             | Pass      |                                        |                               |
|                      | Reset password                               | Page displays showing password is reset and user can login with new password | Pass | |                          |
|                      | Enter username and password correctly        | User is logged in                              | Pass      |                                        |                               |
|                      | Log in                                       | User is returned to homepage                   | Pass      |                                        |                               |
| **Logout Page**       |                                             |                                                 |           |                                        |                               |
|                      | Click log out from Navbar or My Account icon | User is brought to sign-out confirmation page   | Pass      |                                        |                               |
|                      | Confirm sign out                             | User is logged out                            | Pass      |                                        |                               |
| **Admin Actions**     |                                             |                                                 |           |                                        |                               |
|                      | Admin approves testimonial                   | Testimonial appears on course detail page      | Pass      |                                        |                               |
|                      | Admin views course contents page             | Buttons display to edit or delete course       | Pass      |                                        |                               |
|                      | Admin views course detail                    | Buttons display to edit or delete course       | Pass      |                                        |                               |
|                      | Admin clicks edit course from course contents page | Admin is brought to edit course page and message notifies which course is being edited | Pass | |                           |
|                      | Admin clicks edit course from course detail page | Admin is brought to edit course page and message notifies which course is being edited | Pass | |                           |
|                      | Admin clicks cancel from edit course page     | Admin is brought to course contents page      | Pass      |                                        |                               |
|                      | Admin makes edit from edit course page        | Admin is brought to course detail page, edit is made and message appears saying course updated successfully | Pass | |                     |
|                      | Admin clicks delete course from course contents page | Confirmation page appears                 | Pass      |                                        |                               |
|                      | Admin clicks delete course from course detail page | Confirmation page appears                 | Pass      |                                        |                               |
|                      | Admin confirms course is to be deleted        | Admin is brought to course contents page, course is deleted and message appears confirming this | Pass | |                     |
|                      | Admin makes edit from edit course page        | Admin is brought to course detail page, edit is made and message appears saying course updated successfully | Pass | |                     |
|                      | Admin clicks My Account icon                  | Course Management Option displays            | Pass      |                                        |                               |
|                      | Admin clicks Course Management option         | Admin is brought to Course Management Page   | Pass      | Font color is not fitting with overall theme of site |                 |
|                      | Admin clicks cancel on Course Management page | Admin is brought to course contents page      | Pass      |                                        |                               |
|                      | Admin submits a new course from Course Management page | Admin is brought to new course detail page and message appears confirming course has been added | Pass | |             |
|                      | Non-logged in user enters delete course confirmation or delete course URL | User is brought to sign-in page | Pass | |                             |
|                      | Non-Admin user enters delete course confirmation or delete course URL | Message displays saying only admins can do that | Pass | |                             |
|                      | Non-logged in user enters edit course URL    | User is brought to sign-in page                | Pass      |                                        |                               |
|                      | Non-Admin user enters edit course URL        | Message displays saying only admins can do that | Pass      |                                        |                               |
|                      | Non-logged in user enters add course URL     | User is brought to sign-in page                | Pass      |                                        |                               |
|                      | Non-Admin user enters add course URL         | Message displays saying only admins can do that | Pass      |                                        |                               |


### Browser Testing
The site was tested and was confirmed to display correctly, be responsive and comatible with the follwoing browsers:
- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/browsers/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge?ep=192&form=MA13L1&es=40))

### Device Testing
The site was tested and was confirmed to display correctly and be responsive on the following devices:
- Desktop Computer
- iPhone 14 Pro Max - during testing on this device it was discovered that the "My Account" drop-down menu was hidden behind the fotter in the collapsed navbar view. This was fixed.
- Galaxy S8
- IPAD Pro
  
### User Testing
The website link was provided to 2 users all of whom were able to use the site easily and navigate the site without issue. 

### Bugs
#### Solved Bugs
See comments section of manual testing. 

#### Remaining Bugs


## Features to be Implemented
It is planned to include a blog page with periodical posts giving poker tips. This will serve the purpose of providing content which can be posted on social media and via our newsletter to promote the site to potential users. This should also help improve search engine optimisation as it will give our site further authority and expertise on the subject of poker coaching.

## LIBRARIES AND TOOLS
The following libraries and tools were used:
- Django
  - Allauth
  - Messages
  - Crispy Forms
- Python
- HTML & CSS
- Javascript
- Bootstrap
- Cloudinary
- Font Awesome
- Google Fonts
- Elephant SQL
- gunicorn
- whitenoise  

## DEPLOYMENT

In order to deploy the website he following steps were followed:

### Create App
- From the Heroku dashboard, create a new app;
  
### Attach the PostgreSQL Database (Assumed to be using ElephantSQL.com)
- Access ElephantSQL dashboard;
- Click "Create New Instance";
- Name your plan, select Tiny Turtle (free), leave Tags field blank;
- Click "Select Region" and choose local data center (for me EU-West-1 (Ireland));
- Click "Review";
- Check details are correct and then click "Create Instance";
- Return to dashboard and click on Database Instance Name for your project;
- Copy database URL;
  
### Prepare environment and settings.py files
- In workspace create env.py file (add to .gitignore file);
- Add "Import os" to env.py;
- Add a blank line, then set a DATABASE_URL variable, with the value copied from ElephantSQL as follows: os.environ["DATABASE_URL"]="<copiedURL>";
- Add following text including your chosen secret key:  os.environ["SECRET_KEY"]="<your chosen secret key goes here between the quotes>";
- Save the file;
- Now to make your Django project aware of the env.py file, open settings.py and add the following below you Path import:
```
import os
import dj_database_url
if os.path.isfile('env.py'):
import env
```

- Further down remove secret key provided by Django and instead reference key you chose in your env.py file as follows:  SECRET_KEY = os.environ.get('SECRET_KEY');
- Next to hook up the database scroll down to database section in settings.py;
- In place of the Database variable add the following:
```
  DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 	}
```
- Save the file and run "python3 manage.py migrate";
  
### Set up Heroku Config Vars
- Navigate to settings tab;
- Create confg var with key "DATABASE_URL" and for  value copy and paste your database URL (for me this was from ElephantSQL);
- Create config var with key "SECRET_KEY" and for value add your secret key "********" which is referenced in the settings.py file in your env.py file.
- Create config var with key "PORT" and value "8000" - click add;
  
### Get static and media files stored on Cloudinary
- Create Cloudinary account;
- At dashboard copy API Environment Variable URL;
- Return to env.py file and add the following; os.environ["CLOUDINARY_URL"] = "<your cloudinary url minus "CLOUDINARY_URL=">";
- Copy this value and return to Heroku;
- Create a config var with key "CLOUDINARY_URL" and for the value add the URL you copied above;
- Create config var with key "DISABLE_COLLECTSTATIC" and for value set as "1";
- Return to settings.py file and to add in Cloudinary Libraries add "cloudinary_Storage" to the list of INSTALLED_APPS just above "django.contrib.staticfiles". Then add "cloudinary" underneath;
- Towards end of settings.py add the following:
```
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cludinary_storage.storage.MediaCloudinaryStorage'
```

### Tell Django where templates are stored
- Under BASE_DIR add the following: TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates');
- Scroll down midway and add "TEMPLATES_DIR" as the DIRS key in the TEMPALTES setting;

### Add Heroku host name to Allowed Hosts
- In settings.py add "<your heroku app name>.heroku.com", "local host" to ALLOWED_HOSTS

### Tell Heroku how to run project
- create a "Procfile;
- Add the following to the file: web: gunicorn <your app name>.wsgi;
- save files, add commit and push to repository;

### Deployment
- Return to Heroko;
- Navigate to Deploy tab;
- Select GitHub as deployment method;
- search for your repository;
- Scroll down and click "Deploy Branch";
- If you like you can choose to enable automatic deploys;



## CREDITS
Code and direction for the Search Function was taken from this [tutorial](https://www.youtube.com/watch?v=AGtae4L5Bb) provided by Codemy.com.

Code and direction for the Javascript and Modal function was taken from the Code Institute's Django Blog Webinar.

Code and direction for the messages feature was taken from the Code Institute's I think therefor I Blog module.

Code and Direction for part of admin.py file were provided by users Francisco and catavaran on [Stack OverFlow](https://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin).

Inspiration for the Star Rating feature was taken from Arron Beale's "number of guests" feature in his Portfolio Project 4 [The Diplomat](https://github.com/ArronBeale/CI_PP4_the_diplomat)

Code and direction for the comment model and views were taken from [codepiep](https://www.youtube.com/watch?v=ScABStHY8cc&t=5s).

All photographs were provided by [Pexels](https://www.pexels.com/) and minified with https://app.imagify.io/

Thanks to:
- Code Institute for providing the Gitpod template.
- Dick Vlaanderen for his mentoring support
- The Code Institute Tutor Support 

		




