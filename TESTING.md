# Table of Content
- [Validation](#validation)
- [Manual Testing](#manual-testing)
- [User Testing](#user-testing)
- [Bugs](#bugs)
- [Features to be Implemented](#features-to-be-implemented)

Return back to [README.md](README.md).

# Validation

## HTML - No errors were returned when code was checked with the official [W3C validator](https://validator.w3.org/), save for:
  - On Coach Bios and Course Details page there are "No p elements in scope but a p end tag is seen" errors - i believe this is not correct and has been picked up because of the markdown being provided by django Summernote.

| Page                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Courses**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/a4dbc9ab-3a73-4b9c-8b32-4c4453072244) | No Errors  |
| **Our Team**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/35ab86bb-5752-467a-aa56-4d021ff6caf1) | Errors due to Summernote markdown  |
| **Sign Up**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7e35c0ba-27ab-49af-8a46-2f951154ad9f) | Warning due to h1 in callout  |
| **Login**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0c15fa93-9e24-4665-84ce-d05dd60eda9a) | Warning due to h1 in callout  |
| **Profile**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9e427b6f-f376-4b6a-8cbf-18367071c75f) | Warning due to h1 in callout, Cannot resolve Info issue as trailing slash does not appear in profile.html or when viewing page source. Possible cause is to do with redirect where W3C is not a logged in user so will review ny direct input below  |
| **Profile (via Direct Input)**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9d50669d-796a-4390-b827-649da96ebfb5) | No Errors  |
| **Shopping Cart**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/5f5c59e3-544e-48da-9304-afbd86c9b9f6) | No Errors  |
| **Course Detail**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/fcd805f7-c52a-4ab6-989e-c98a74c73b17) | Errors due to Summernote markdown  |
| **Password Reset**   | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7b763fc4-d5c1-4431-a52b-d875b1f0ec77) | Warning due to h1 in callout  |
| **Checkout (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/a01ce906-cc27-421e-8f37-829444f49154) | Warning due to h1 in callout and empty h1 in loading spinner  |
| **Checkout Success (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/acfd2c18-d934-4a28-a971-39517d39c4c0) | No Errors  |
| **Add Course (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/574dde69-84d7-44ac-9600-c470f0617054) | No Errors  |
| **Edit Course (via Direct Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7d5c0a7a-b3af-43d1-b9e2-1ebfed836851) | H1 warning due to empty Callout  |
| **Delete Confirmation (via Direct Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/13a30666-826e-43f8-b7ab-094c4079a338) | H1 warning due to empty Callout  |



## CSS - No errors were returned when code was checked with the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Base.css**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/64820e45-9e28-4631-8bbd-592e25958dc6) | No Errors  |
| **Checkout.css**     | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7b8b7fe8-15a9-4a83-921b-6b3bea59378d) | No Errors  |

## JAVASCRIPT - No errors were returned when code was checked with the official [JS Hint validator](https://jshint.com/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **stripe_elements.js** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/12bb22e1-c0e9-46a9-a5c5-b95448e3dbf4) | No Errors  |


PYTHON - No errors were shown when code was checked with the Code Institute Python Linter (https://pep8ci.herokuapp.com/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Bag - apps.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/40cdbab8-7f8b-48a3-9213-5112b90a752d) | No Errors  |
| **Bag - contexts.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/81e4a933-7505-4d12-b2f0-7412b7a58e48) | No Errors  |
| **Bag - test.views.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/21542e3c-a7f8-4ce2-957a-b23126c8cfd7) | No Errors  |
| **Bag - urls.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0cb5e89f-f534-4fe7-b9b2-7747fcc05e8e) | No Errors  |
| **Bag - views.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/994f1f81-636f-430f-a0d6-2940d4838821) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |


Accessibility - I confirmed the code used is accessible by using lighthouse in devtools.

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/01264a54-18ba-4e4c-bcb7-4e8885249d30)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/eb00dac5-2ab8-433e-9f1a-dcfcba18e3a8)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/067b018d-e7cb-431e-8ff2-9e8a3663c775)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e55cd2df-c975-4d81-ba06-786736b6de69)





# Manual Testing
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


# Browser Testing
The site was tested and was confirmed to display correctly, be responsive and comatible with the follwoing browsers:
- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/browsers/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge?ep=192&form=MA13L1&es=40)

# Device Testing
The site was tested and was confirmed to display correctly and be responsive on the following devices:
- Desktop Computer
- iPhone 14 Pro Max - during testing on this device it was discovered that the "My Account" drop-down menu was hidden behind the fotter in the collapsed navbar view. This was fixed.
- Galaxy S8
- IPAD Pro
  
# User Testing
The website link was provided to 2 users all of whom were able to use the site easily and navigate the site without issue. 

# Bugs
## Solved Bugs
See comments section of manual testing. 

## Remaining Bugs
None known.

# Features to be Implemented
It is planned to include a blog page with periodical posts giving poker tips. This will serve the purpose of providing content which can be posted on social media and via our newsletter to promote the site to potential users. This should also help improve search engine optimisation as it will give our site further authority and expertise on the subject of poker coaching.
