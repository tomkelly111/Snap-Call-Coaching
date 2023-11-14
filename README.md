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


### Goal and Business Plan
The goal of the website is to sell online poker coaching courses to all level of players. Courses range from absolute beginner right through to aspiring proffessionals. Price ranges for the courses reflect the level of expertise covered. 

In designing the site these content questions were considered and answered as follows:

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

In determining the marketing of the site these questions were considered and answered:

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
The website was designed with simplicity in mind. There is minimal clutter with the focus being on the courses themselves. The font [Kanit](https://fonts.google.com/specimen/Kanit) was chosen as it adds to the minimalist feel of the site while also haveing a computational / mathematical theme which compliments our course content. [It is a combination of concepts, mixing a Humanist Sans Serif motif with the curves of Capsulated Geometric styles that makes it suitable for various uses, contemporary and futuristic.](https://fonts.google.com/specimen/Kanit/about). For the color design, Green was chosen as it is reflective of the green felt of a poker table. The greys and blacks compliment the dark green color and were taken from palettes available on [Color Space](https://mycolor.space/).

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
- As a **User** I can **view available courses** so that **choose which course suits me best**.
- As a **site owner** I can **provide a function where users can sign up for weekly emails** so that **I have a database of customers to whom I can make offers**.
- As a **User** I can **use a nav bar** so that **easily navigate to different sections of the site**.
- As a **user** I can **view details and bio of all coaches** so that **i can be assured of the quality of the courses**.
- As a **admin** I can **CRUD courses on the front end** so that **I can easily update the site with new courses as they become available**.
- As a **site owner** I have **a facebook business page** so that **I can market the business**.
- As a **User** I can **create an account** so that **I can access materials purchased**.
- As a **developer** I have **included key words throughout the site's code** so that **the site will rank highly on search engines**.
- As a **user** I can **purchase a course** so that **I can access the course materials**.
- As a **user** I can **see a 404 page when there is an error** so that **the site feels fully functional**.
- As a **user** I can **receive messages throughout the site** so that **i know what actions i have taken**.

#### Should Haves (completed)
- As a **User** I can **see a clear description of the site and what it offers** so that **I can immediately know if I am interested in what the site offers**.
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
#### Homepage
The homepage displays the most recently added coffee shop posts paginated by three. On first arrival the navbar provides the options to register or login. The option to add a coffee shop is displayed but this is only actie for logged in users.
Each post dispalys an image, the shop name, location, a short description and who it was posted by. If users wish to they can click "read reviews" to read a full review and see comments.

There is a search function which allows users to search for coffee shops. Results matching the search parameters will be displayed and if there are no available results users are given the option of adding a coffee shop themselves.

![image](https://github.com/tomkelly111/Beansters/assets/111172617/5b128e80-06fe-4986-a41a-6a1cc0e4ee7b)

#### Post Detail
Once a user clicks "read reviews" on a post they are taken to the post detail view. Here they can see a full review of the coffee shop as made by the original poster. Here they will also be able to read comments which have been added by other users. If the user has logged in they will be able to add additional comments themselves.

<img width="943" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/c6b509df-a59b-4645-8277-3af8a185d801">

#### Add a Coffee Shop
If users are logged in they have the option to add a coffee shop by clicking "Add a Coffee Shop" in the navbar. Once clicked the user is taken to a form where they can fill out the details of the coffee shop, provide a review and upload an image to accompany their post. They can provide a location and a brief description as well as a star rating in order to provide a summary of their review.

<img width="956" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/0d798b81-c678-4683-94c1-c90e06258cfc">

#### Add a Comment or Review
Logged in users can can add commnents to other users posts in order to make a comment on other's reviews or add their own review and star rating if they have visited that coffee shop themsleves.

<img width="647" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/127db608-7f61-4e06-87d5-24a15ce0bf06">

#### Register / Login
Users have the ability to register or login. Once they have done so they have the ability to post reviews or add comments.


<img width="377" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/767cbf50-9bf7-4d96-a482-5bb1b3776b34">


<img width="603" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/d383e5bb-3036-44a9-9d79-1dd34bf80953">

#### Confirmations
The site offers users confirmations and feedback throughout to ensure the user knows what they are doing. There are confirmations for logging in, logging out, adding or editing a post (notifying the user that their post will appear once it has been approved) and adding a comment (same as for a post). When a user chooses to delete a post a modal will appear asking them if they are sure they want to delete as this cannot be undone.

<img width="454" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/0f99d720-2841-49b5-9504-f348dd3c26fd">

#### Search
The site has a search function which allows users to search for coffee shops. Once a search is completed matching posts are displayed and the user can click in to read more. If there are no results, this is displayed and the user is invited to add the coffee shop themselves.


<img width="686" alt="image" src="https://github.com/tomkelly111/Beansters/assets/111172617/66cd6ac7-4236-4ba0-a3bc-0d7731eea307">



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

### Database & Models

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/ed14259c-2282-4668-a266-038ff62d8ced)

<table>  
        <tr>
              <th>Coffee Shop Post</th>
            </tr>    
	<tr>
              <th>Name</th>
              <th>Type</th>
            </tr>
            <tr>
              <td>Shop</td>
              <td>CharField (unique)</td>
            </tr>
            <tr>
              <td>Description</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Review</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Author</td>
              <td>ForeignKey</td>
            </tr>
            <tr>
              <td>created_on</td>
              <td>DateTimeField</td>
            </tr>
            <tr>
              <td>featured_image</td>
              <td>CloudinaryField</td>
            </tr>
	<tr>
              <td>Approved</td>
              <td>BooleanField</td>
            </tr>
	<tr>
              <td>Location</td>
              <td>Charfield</td>
            </tr>
	<tr>
              <td>Rating</td>
              <td>Integerfield</td>
            </tr>
</table>

<table>  
        <tr>
              <th>Comment Model</th>
            </tr>  
	<tr>
              <th>Name</th>
              <th>Type</th>
            </tr>
	<tr>
              <td>Post</td>
              <td>ForeignKey</td>
            </tr>
            <tr>
              <td>Name</td>
              <td>CharField</td>
            </tr>
            <tr>
              <td>Email</td>
              <td>EmailField</td>
            </tr>
            <tr>
              <td>Body</td>
              <td>TextField</td>
            </tr>
            <tr>
              <td>created_on</td>
              <td>DateTimeField</td>
            </tr>
            <tr>
              <td>Approved</td>
              <td>BooleanField</td>
            </tr>
	<tr>
              <td>Rating</td>
              <td>Integerfield</td>
            </tr>
</table>

### Validation

HTML - No errors were returned when code was checked with the official [W3C validator](https://validator.w3.org/), save for one (error stray end tag <div> on the Home Page) but I beleive this is incorrect and is arising due to the use of block content.


CSS - No errors were returned when code was checked with the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/).


JAVASCRIPT - No errors were returned when code was checked with the official [JS Hint validator](https://jshint.com/).


PYTHON - No errors were shown when code was checked with the Code Institute Python Linter (https://pep8ci.herokuapp.com/) save for 2 errors in settings.py where lines were too long.


Accessibility - I confirmed the code used is accessible by using lighthouse in devtools although at times performance dips into the 80s % but i believe this may be due to poor internet connection.



## TESTING

### Manual Testing
#### Homepage
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>last three posts are displayed in 3 columns all links work</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>All nav bar links work but "add coffee shop post" link is inactive when user is logged out</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>View hompage</td>
              <td>Footer sits at bottom of page and all icon links work</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Use search bar</td>
              <td>Successful search returns result</td>
              <td>Pass</td>
            </tr>
	<tr>
              <td>Use search bar</td>
              <td>Unsuccessful search returns prompt to add coffee shop</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Click "Read reviews" button on post</td>
              <td>Brings user to post detail view</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Click Login</td>
              <td>Brings user to login page</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Click Register</td>
              <td>Brings user to register page</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Click Add a Coffee Shop</td>
              <td>Brings user to new post page</td>
              <td>Pass</td>
            </tr>
</table>

#### Register Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Register in Nav Bar</td>
              <td>Sign Up form is displayed</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Sign Up</td>
              <td>Message alert says sign in was successful</td>
              <td>Pass</td>
            </tr>
</table>

#### Login Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Login in Nav Bar</td>
              <td>Login form is displayed</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Login</td>
              <td>Message alert says login was successful</td>
              <td>Pass</td>
            </tr>
</table>

#### Login Out Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Logout in Nav Bar</td>
              <td>Logout confirmation is displayed</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Logout</td>
              <td>Message alert says logout was successful</td>
              <td>Pass</td>
            </tr>
</table>

#### Add a Coffee Shop Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>User logged out - Click Add a Coffee Shop in Nav Bar</td>
              <td>Link inactive</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>User logged in - Click Add a Coffee Shop in Nav Bar</td>
              <td>Brings user to new post page</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Create Post</td>
              <td>Message alert says post will appear once approved and user is returned to Homepage</td>
              <td>Pass</td>
            </tr>
</table>

#### Post Detail Page
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Click Read Reviews on post on Homepage</td>
              <td>Brings User to Post Detail page</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Edit / Delete</td>
              <td>If user is author of post there should be options to edit or delete post</td>
              <td>Pass</td>
            </tr>
	<tr>
            <td>Click Edit</td>
              <td>User is brought to Edit Post page</td>
              <td>Pass</td>
            </tr>
            <tr>
            <td>Edit Post</td>
              <td>User is returned to Homepage and message alert displays stating post is waiting approval</td>
              <td>Pass</td>
            </tr>
            <tr>
            <td>Delete Post</td>
              <td>Modal should appear asking user to confirm as deletion cannot be undone</td>
              <td>Pass</td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>If user is not logged in text should display asking them to login or register in order to post a comment</td>
              <td>Pass</td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>If user is  logged in comment form should display</td>
              <td>Pass</td>
            </tr>
            <tr>
            <td>Add Comment</td>
              <td>Once User adds comment, a message alert should display stating their comment is awaiting approval</td>
              <td>Pass</td>
            </tr>
</table>

#### Page Layout
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Mobile - Home page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Post Detail page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Register page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Login page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Logout page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Add a Coffee Shop page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Edit Post page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Mobile - Search page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
</table>

<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Desktop - Home page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Post Detail page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Register page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Login page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Logout page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Add a Coffee Shop page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Edit Post page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
            <tr>
              <td>Desktop - Search page</td>
              <td>Layout is displayed correctly</td>
              <td>Pass</td>
            </tr>
</table>


### User Testing
The website link was provided to 3 users all of whom were able to use the site easily and navigate the options without issue. The rating system was liked by all users. Some feedback was recieved that they would like to be able to view their account details or change password. 

### Bugs
#### Solved Bugs
During testing an error was discovered whereby users could not sign up. This was due to formatting in the settings.py file where code was altered to fit on one line. This bug was resloved. 

#### Remaining Bugs
When a user leaves a comment a message appears saying their comment is awaiting approval. If they refresh the page the comment is submitted again. This will be addressed in the next iteration.

## Features to be Implemented
When a user logs in to comment on a post they are brought to the homepage instead of back to the page they were viewing. This will be addressed during the next iteration so that the user is returned to the page they intended to comment on.

When a user chooses to edit a post there is no way to cancel except for exiting the page. This will also be addressed in the next iteration.

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

		




