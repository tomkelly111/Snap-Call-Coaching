![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

...............................................
# [Snap Call Coaching](https://snapcallcoaching-146b3f7fc4be.herokuapp.com/)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/f95cf299-1b94-4f00-919d-7dd121319b86)


[Snap Call Coaching](https://snapcallcoaching-146b3f7fc4be.herokuapp.com/) is a website which sells online poker coaching services. It is aimed at all levels of players from absolute beginner right through to aspiring profesionals. 


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

- [Database & Models](#database-and-models)
  
- [Testing](#testing)
  
- [Libraries and Tools](#libraries-and-tools)
- [Deployment](#deployment)
- [Credits](#credits)
  


## User Experience


### Goal 
The goal of the website is to sell online poker coaching courses to all level of players. Courses range from absolute beginner right through to aspiring professionals. Price ranges for the courses reflect the level of expertise covered. The courses are structured so that as a user completes the beginners course they will then have the expertise to undertake the intermediate course etc. It is hoped that user will enjoy and benefit from the course and so be encouraged to purchase more advanced courses over time. Contents of courses are also set out so that more advanced players can skip beginner courses and start at whichever course suits their abilities.

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
  - The site will contain profiles of the coaches who will all be professional poker players. Coach bios will list their experience and accolades. This will give them the authority and expertise to teach.
  
- Would there be other pages within the site which we could link to from a chosen page?
  - Each course will list the coaches available and contain links to each coaches profile. Each coaches bio will list the the course they coach on and link to those courses. 

##### In determining the marketing of the site these questions were considered and answered:

- Who are our users?
  - Given the profile of poker players in general our users are likely to be mostly males between the ages of 18 - 45
    
- Which online platforms would we find lots of our users?
  - Many of our users would be frequent users of the larger poker playing sites such as PokerStars, GGPoker and 888Poker. They will also browse online forums such as twoplustwo and r/poker on reddit. 
  
- Would our users use social media? If yes, which platforms do you think you would find them on?
  - Typically our users would use YouTube to view poker content as well      as a smaller market on instagram and tiktok.

- What do our users need? Could we meet that need with useful content? If yes, how could we best deliver that content to them?
  - Yes, our users would be looking to learn better poker skills. This can be provided via our online training courses.
    
- Would our business run sales or offer discounts? How do you think your users would most like to hear about these offers?
  - Looking at other similar business models, we will offer a newsletter that provides poker tips and strategies for free. Users can subscribe to this newsletter via email. These emails can also be used to offer discounts and promote newly added courses to our user        base.
    
- What are the goals of our business? Which marketing strategies would offer the best ways to meet those goals?
  -  The goal of the business is to sell our courses. The best marketing strategy for this starting out (for budget reasons) would be free/ low cost. It is intended to use our newsletter service as a means of promotion. Once we have a bigger user base and more budget       it is intended to market our site on the various poker forums and poker videos appearing on YouTube.
  -  As the site grows it maybe possible to approach popular professional players with whom we can pay to promote our courses on their social media.
  -  Additionally, we will include a feature where users who have purchased a course can leave a testimonial as to their experience with the content. This will serve        as a reasurance to prospective purchasers that we provide high quality content. 



### Design
The website was designed with simplicity in mind. There is minimal clutter with the focus being on the courses themselves. The font [Kanit](https://fonts.google.com/specimen/Kanit) was chosen as it adds to the minimalist feel of the site while also having a computational / mathematical theme which compliments our course content. [It is a combination of concepts, mixing a Humanist Sans Serif motif with the curves of Capsulated Geometric styles that makes it suitable for various uses, contemporary and futuristic](https://fonts.google.com/specimen/Kanit/about). For the color design, Green was chosen as it is reflective of the green felt of a poker table. The greys and blacks compliment the dark green color and were taken from palettes available on [Color Space](https://mycolor.space/). 

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/24fc708d-0103-4820-8cdc-2e6b414a341b)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/ef77f427-9be5-44a6-ad03-ad05a67f9c13)

The logo was designed using [Logo.com](https://logo.com/).

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/282c32a5-ec2c-4052-8a5b-c6e17e442ff6)


#### Wireframes
Wireframes were created using [https://app.moqups.com/](https://app.moqups.com/).

- Landing Page
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/85436c34-1379-495f-bae5-65dff73f6a78)

- Courses
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9e5f35c9-4483-4fde-85ab-9bce0bd7ad86)

- Course Detail
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0ef0a154-ab29-4a6f-97b5-737308287a25)

- Our Team
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/93bd9cd1-074b-4ade-9f35-f3e06dc2c1d7)

	

### User Stories
Agile methodoligies were used to plan and design the website. User stories were created using issues on GitHub and were added  to five epics (milestones):
- Epic 1: Landing Page
- Epic 2: Courses
- Epic 3: Coaches
- Epic 4: Marketing
- Epic 5: Additional Functionality
	  
	
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/6c2f393e-9258-48b3-9d0d-e641e52c496d)

- These epics were broken down into user stories which were labeled and categorised in accordance with MoSCoW principles.

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/60cc54ab-893f-41f7-a20f-d3ba3511806e)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/dc390ca1-4a94-455c-9515-78aaa7f63edf)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/97f2873b-df61-4921-b3de-b9ac62406a8d)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/300edfad-bee2-4f4f-9f7d-7f1c9a4189b1)


![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/4792c082-c3d8-44ac-8f1e-a4d17929bce7)


- The progress of these user stories were tracked via the use of the GitHub kanban-board. 
	
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d03ee81a-18c1-4fb9-acb2-19aecc553d53)
	
	
While the use of agile methodologies was useful in staying on track with the project, on reflection some of the user stories should have been broken down into smaller user stories to make them more manageable.	

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



Each user story was assigned tasks in order to complete it, these were set out as follows:

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/04650cf6-d67c-4281-bc13-95772a4c63e4)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/6f79604f-cdcc-4f4c-aa95-659bea0280be)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/c9c76d6b-aec2-4177-bfb7-0f1adf08eb18)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/25d63893-274d-4811-bce1-313d1d077a86)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e9f49bc3-7847-4089-b981-b7b835b6fd56)



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

	On smaller devices the navbar collapses into a burger icon but all features are still available.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/f01a132e-6c03-4f05-b0ee-bc441b862fa4)

- #### Callout
	At the top of each page there is a callout which using template literals is customizable for each page it displays on.

	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/1de441a9-d0cd-402b-bae8-10a8f704e614)

- #### Landing Page

	The Landing page displays a description of the site and what it offers followed by a link to view our courses. There is also a poker tips signup form provided by [Mail Chimp](https://mailchimp.com/).

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
	
	Where the user is a site admin, buttons will also display the options to edit or delete the course:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/f4dc26dd-f7ad-4cba-81db-9f8f6ed8280e)


- #### Course Detail
	The Course Detail page displays the content of each course taken from the COURSE Model. There is the name, brief description, a longer detailed description of the contents and links to the coaches for that course. There are also two buttons, one to return the other courses and one to purchase the course which when clicked automatically adds the course to the users cart and redirects the user to the cart page. A pop up message will also display saying the course has been added to the cart.
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/55406f04-c130-4151-bb5c-f96f3aab264a)

	
	Mobile View:
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7fee9074-6b1e-487d-9d76-f5dc594dab6c)

	
	If a user has purchased a course then there is an option to add a testimonial of their experience on the course. Once submitted via the TESTIMONIALS Model, this needs to be approved by a site admin after which it will appear on the other side of the screen. Once a user has submitted a testimonial the option to submit one no longer appears.
	
	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/12082938-7ede-47b1-90e8-5b7abca20a0f)

	
	If the user is a site admin then buttons to edit or delete the course also display here. If the user has already purchased this course then the purchase now button is removed and instead they see the following option:
	
	![image](https://github.com/tomkelly111/trialworkspace/assets/111172617/bc54ef7b-ebf4-4bb2-95fd-44916af0b5c4)
	

- #### Our Team
	The Our Team page displays all of the coaches that are currently providing their services taken from the COACH Model. Each post displays the name and biography of the coach along with a profile picture and a list of their accolades. The courses they are coaching on are also linked. New coaches can be added by site admins via the admin panel.
	
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
	Users who wish to register can do so by clicking the link in the navbar or on the dropdown menu of the My Account icon. Once they do so they are taken to the Sign Up page where they are asked to register their details. Once submitted, the user is prompted to check their email for a verification email where they can click a link to confirm this is a valid email address.
	
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
	Admin users can access the Course Management page from the dropdown menu on the My Account icon. Once on the Course Management page admins can upload a new course using the COURSE Model. Once the new course is added the admin user is redirected to the course detail view of that course and a message popsup saying course was successfully added.

	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/bb79dea5-6109-468e-bd5a-ffa9004e957c)

- #### Messages
	The site is equipped with messages throughout to guide the user at all stages of their experience. Examples are below:
	
	<img width="196" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/56369f38-a815-4dfe-b52e-3299f7bbe87f">
	
	<img width="284" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/13b0b5a2-6ddf-418d-9849-edaa6e533a0d">
	
	<img width="209" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/94d84dc4-55d6-4a27-93b8-8699b288d2ca">

- #### 404 Page
	The site has a custom 404 page that displays is the user lands on a page that does not exist. This includes a button to return home.

	![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e297f979-f79d-40d8-8ef0-0004f18b383c)

- #### Stripe
	[Stripe](https://stripe.com/ie) is used in order to take payments from customers on the site. This was implemented following along with Code Institute's Boutique Ado walkthrough Project. The site also implements webhooks which assist with:
	- sending confirmation emails
 	- updating users profile details
  	- completing orders and adding them to the database if there is an issue with for example user's browser crashing

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


## DATABASE AND MODELS

The below database schema was designed using [DrawSQL](https://drawsql.app/). This was of assistance in visualising the layout of the models to be used.

<img width="556" alt="image" src="https://github.com/tomkelly111/trialworkspace/assets/111172617/6b6984e6-0371-49d8-9f79-661cd3bfde0b">


## TESTING
For testing writeup please view [TESTING.md](TESTING.md).


## LIBRARIES AND TOOLS
The following libraries and tools were used:
- Django
  - Allauth - For user accounts
  - Messages - For success / error / infor messages and confirmations
  - Crispy Forms - for all forms e.g. Add Course, Update billing details
  - Summernote - for styling of text via the admin panel
  - Countries - to select a country
- Python
- HTML & CSS
- Javascript
- Bootstrap
- Font Awesome
- Google Fonts
- Elephant SQL - database
- Pillow - handling images
- gunicorn - running Python web applications
- Stripe - for receiving payments
- Amazon AWS - for storing static files
- GMAIL API - for sending confirmation emails
- [https://www.simpleimageresizer.com/](https://www.simpleimageresizer.com/) - for resizing images

## DEPLOYMENT

In order to deploy the website he following steps were followed:
  
### Attach the PostgreSQL Database (Assumed to be using ElephantSQL.com)
- Access ElephantSQL dashboard;
- Click "Create New Instance";
- Name your plan, select Tiny Turtle (free), leave Tags field blank;
- Click "Select Region" and choose local data center (for me EU-West-1 (Ireland));
- Click "Review";
- Check details are correct and then click "Create Instance";
- Return to dashboard and click on Database Instance Name for your project;
- Copy database URL;

### Create App
- From the Heroku dashboard, click create a new app;
- Give the app a name and select region;
- Click create app;
- Open settings tab;
- Create config var called "DATABASE_URL" and copy in the database URL from PostgreSQL for the value;

  
### Prepare environment and settings.py files
- In terminal install dj_database_url and psycopg2 by typing in "pip3 install dj_database_url==0.5.0 psycopg2";
- Update requirements.txt by typing "pip freeze > requirements.txt";
- In settings.py add "import dj_database_url" under "import os";
- In the Database section of settings.py comment out as follows:
```
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': BASE_DIR / 'db.sqlite3',
 #     }
 # }
```

and instead add the following while inserting your database url:

```
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```

- In the terminal type "python3 manage.py showmigrations" to confirm you are connected to the database, if you are you should see a list of migrations with none of the checked off;
- Type in the termina "python3 manage.py migrate" to migrate your models to the new database;
- Type "python3 manage.py createsuperuser" and follow the steps to create a superuser for the database;
- To prevent the databse from being exposed when we push to GitHub, revert the database text in settings.py to the following:
```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

- To confirm the data in your database has been created go to the ElephantSQL page for your database and on the left select "Browser";
- Click the table queries button and select auth_user;
- When you click execute you should see newly created superuser details displayed, this confirms your database has been set up;

### Deploying to Heroku
- So that when site is running on Heroku we connect to Postgres and otherwise we connct to sqlite add the following if statement to settings.py:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

- Next install gunicorn by typing "pip3 install gunicorn" into the termional;
- Update requirements.txt by typing "pip freeze > requirements.txt";
- create a "Procfile;
- Add the following to the file: web: gunicorn <your app name>.wsgi;


### Add Heroku host name to Allowed Hosts
- In settings.py add "<your heroku app name>.heroku.com", "local host" to ALLOWED_HOSTS;
- Save files, add commit and push to repository;
  
### Set up Heroku Config Vars
- Navigate to settings tab;
- Create confg var with key "DATABASE_URL" and for  value copy and paste your database URL (for me this was from ElephantSQL);
- Create config var with key "SECRET_KEY" and for value add your secret key "********" which is referenced in the settings.py file in your env.py file.
- Create config var with key "PORT" and value "8000" - click add;
- Create config var with key "DISABLE_COLLECTSTATIC" and for value set as "1";
- Include Stripe keys (Publishable Key and Secret Key) if used in project;

### Deployment
- Return to Heroko;
- Navigate to Deploy tab;
- Select GitHub as deployment method;
- search for your repository;
- Scroll down and click "Deploy Branch";
- If you like you can choose to enable automatic deploys;

### Setting up AWS
- Navigate to [aws.amazon.com](aws.amazon.com);
- Create an AWS account;
- On account type page select personal and fill in details, click create account;
- Enter credit card details;
- Answer verification questions and create account;
- Return to [aws.amazon.com](aws.amazon.com) and access management console under my account and sign in;
- Search for S3;
- Create new bucket and name it e.g."heroku-app-name";
- Select closest region;
- For object ownership select "ACLs Enabled";
- For Onject Ownership select Bucket Oner Preferred";
- Other requirements can be left as default;
- Unselect block public access;
- Create bucket;
- Click into newly created bucket and open the properties tab;
- Scroll down and enable static website hosting (index hosting can be set as index.html);
- Navigate to permissions tab;
- Paste in the following for the CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Edit policy and click policy generator;
- select S3 policy type;
- Add "*" to select all principals;
- Select "Get Object" for action;
- Copy ARN from bucket policy tab;
- Paste into ARN box;
- Click add statement and then generate policy;
- Copy policy and paste into Bucket Policy editor;
- Add "/*" onto end of resource key to allow access to all resources;
- Save;
- Scroll down to Access Control List and click edit;
- Enable List for Everyone (public access) and accept warning;
- Create a user by navigating to services menu and going to IAM;
- Click User Groups and then Create Group;
- Enter group name;
- Click create group;
- Click into newly created group and nnavigate to permissions tab;
- Click add permissions and then create inline policy;
- Go to JSON tab;
- Click import policy;
- Search S3 and select "AmazonS3FullAccess" and click import;
- Get bucket ARN and copy to clipboard;
- Paste in as follows including your ARN (YOUR_ARN):
```
"Action": [
                "s3:*"
            ],
            "Resource": [
                "YOUR_ARN",
                "YOUR_ARN/*"
            ]
```

- Click next and enter policy name, click create policy;
- Navigate to User Groups and select group;
- Click permissions tab, add permissions and attach policy;

- Create a user for the group by going to Users on the left hand side;
- Click Add User;
- Create a User e.g. "appname-static-files-user";
- Give the user programatic access and click next;
- Add user to group you just created and click create user;
- Download CSV file for access keys by:
	- Go to IAM and select 'Users'
	- Select the user for whom you wish to create a CSV file.
	- Select the 'Security Credentials' tab
	- Scroll to 'Access Keys' and click 'Create access key'
	- Select 'Application running outside AWS', and click next
	- On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
	- Click the 'Download .csv file' button

### Connect Django to S3
- Type the following into the CLI:
	- pip3 install boto3
 	- pip3 install django-storages
  	- pip3 freeze > requirements.txt
- Add "storages" to installed apps in settings.py;
- Add the following to settings.py:
```
if 'USE_AWS' in os.environ:

    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # override static and media urls in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- In Heroko add these keys (AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY) to the config vars using the details from the previously downloaded csv file;
- Also add Key = USE_AWS and Value = 1;
- Remove DISABLE_COLLECTSTATIC variable;
- Create file called custom_storages.py;
- Add the following code:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- Git add, git commit and git push files.
- Navigate to your S3 bucket on [aws.amazon.com](aws.amazon.com) and if everything worked there should now be a static folder containing your static files;
- Click create folder and name it "media", inside click upload, add files and uplaod your media images, selelct grant public read access, click upload;

### Verify Superuser
- Login to your admin section of your site;
- Click into email addresses;
- Click into superuser email, select verified and primary - save;

### Forking and Cloning

- #### Forking
- In order to fork the repository navigate to the top of the page and where it says "Fork" click the drop down menu. Here click "Create new Fork". Name the new repository and click "Create Fork". You will now have your own copy of the repository saved to your own github account to which you can make your own changes.

- #### Cloning
- In order to clone the site locally navigate to where it says "Code" above the repositary. Click the dropdown menu and select the local tab. Then select HTTPS. Copy the URL (https://github.com/tomkelly111/Snap-Call-Coaching.git). In your CLI type:
- ```git clone https://github.com/tomkelly111/The-Card-Club.git``` and hit enter.

- #### ENV.PY
- You will need to create an env.py file and add the relevant key values:
```
import os

os.environ["DATABASE_URL"] = "*****"
os.environ["SECRET_KEY"] = "*****"
os.environ["STRIPE_PUBLIC_KEY"] = "*****"
os.environ["STRIPE_SECRET_KEY"] = "*****"
os.environ["STRIPE_WH_KEY"] = "*****"
os.environ["EMAIL_HOST_PASS"] = "*****"
os.environ["EMAIL_HOST_USER"] = "*****"
os.environ["AWS_ACCESS_KEY_ID"] = "*****"
os.environ["AWS_ACCESS_KEY_ID"] = "*****"
os.environ["AWS_SECRET_ACCESS_KEY"] = "*****"
```

## CREDITS
- Code and direction for the Order, OrderLineItems and UserProfile models was followed along with from the Code Institute's E-commerce Boutique Ado site.
- All photographs were provided by [Pexels](https://www.pexels.com/)
- Instruction on how to make navbar links "active" was provided by Will Howell on [Stack Overflow](https://stackoverflow.com/questions/39639264/django-highlight-current-page-in-navbar#:~:text=You%20can%20get%20the%20name,class%20if%20the%20url%20matches.&text=I%20had%20a%20simialr%20question,be%20populated%20by%20each%20page)
- Instruction on adding the logo was provided by user Dragosct on [Github](https://github.com/creativetimofficial/material-kit/issues/107)
- Instruction on adding login for unit testing was provided by user Dolphus33 on [Stack Overflow](https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login)
- Instruction on superuser login for unit testing was provided by user Sam Dolan on [Stack Overflow](https://stackoverflow.com/questions/3495114/how-to-create-admin-user-in-django-tests-py)

Thanks to:
- Code Institute for providing the Gitpod template.
- Dick Vlaanderen for his mentoring support
- The Code Institute Tutor Support 
- @Karolis, @Nils and @Szilvi for their support on Slack
		




