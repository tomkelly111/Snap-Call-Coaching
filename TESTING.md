# Table of Content
- [Validation](#validation)
- [Manual Testing](#manual-testing)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Unit Testing](#unit-testing)
- [Bugs](#bugs)

Return back to [README.md](README.md).

# Validation

## HTML
No errors were returned when code was checked with the official [W3C validator](https://validator.w3.org/), save for:
  - On Coach Bios and Course Details page there are "No p elements in scope but a p end tag is seen" errors - i believe this is not correct and has been picked up because of the markdown being provided by django Summernote.

| Page                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Homepage**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5204b0d-3e0a-4ea7-b639-7adf71f8cb6a) | No Errors  |
| **Courses**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/a4dbc9ab-3a73-4b9c-8b32-4c4453072244) | No Errors  |
| **Our Team**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/35ab86bb-5752-467a-aa56-4d021ff6caf1) | Errors due to Summernote markdown  |
| **Sign Up**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/342aca66-30be-4324-a89c-21cbcecb98b0) | No Errors |
| **Login**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/da095b71-aca7-4302-87b8-2b472881ee5a) | No Errors  |
| **Profile (via Direct Input)**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9d50669d-796a-4390-b827-649da96ebfb5) | No Errors  |
| **Shopping Cart**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/5f5c59e3-544e-48da-9304-afbd86c9b9f6) | No Errors  |
| **Course Detail**    | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/fcd805f7-c52a-4ab6-989e-c98a74c73b17) | Errors due to Summernote markdown  |
| **Password Reset**   | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d15cec52-93f5-4dd3-a1fa-23f4b2068fff) | No Errors  |
| **Checkout (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/a01ce906-cc27-421e-8f37-829444f49154) | Warning due to h1 in callout and empty h1 in loading spinner  |
| **Checkout Success (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/acfd2c18-d934-4a28-a971-39517d39c4c0) | No Errors  |
| **Add Course (via Dicrect Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/574dde69-84d7-44ac-9600-c470f0617054) | No Errors  |
| **Edit Course (via Direct Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/b7c24369-b516-45d4-946d-650b3ca94f5b) | No Errors  |
| **Delete Confirmation (via Direct Input)** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/634edd23-47fe-4284-bd6d-a8eb288d7b6e) | No Errors  |



## CSS
No errors were returned when code was checked with the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Base.css**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/64820e45-9e28-4631-8bbd-592e25958dc6) | No Errors  |
| **Checkout.css**     | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7b8b7fe8-15a9-4a83-921b-6b3bea59378d) | No Errors  |

## JAVASCRIPT
No errors were returned when code was checked with the official [JS Hint validator](https://jshint.com/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **stripe_elements.js** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/12bb22e1-c0e9-46a9-a5c5-b95448e3dbf4) | No Errors  |
| **bag.html javascript** | <img width="782" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/930a21fa-daa1-4cb6-9aa6-d60ade1d5813"> | No Errors  |



## PYTHON
No errors were shown when code was checked with the Code Institute Python Linter (https://pep8ci.herokuapp.com/).

| File                 | Result                                      | Comment                                 |
| -------------------- | ------------------------------------------- | --------------------------------------- | 
| **Bag - apps.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/40cdbab8-7f8b-48a3-9213-5112b90a752d) | No Errors  |
| **Bag - contexts.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/81e4a933-7505-4d12-b2f0-7412b7a58e48) | No Errors  |
| **Bag - test.views.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/21542e3c-a7f8-4ce2-957a-b23126c8cfd7) | No Errors  |
| **Bag - urls.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0cb5e89f-f534-4fe7-b9b2-7747fcc05e8e) | No Errors  |
| **Bag - views.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/994f1f81-636f-430f-a0d6-2940d4838821) | No Errors  |
| **Checkout - admin.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/ed8fa8e2-9093-45be-8089-d9c3e47cdfb0) | No Errors  |
| **Checkout - forms.py**  | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0914ddf7-90d9-46bd-9c56-15d31328e75b) | No Errors  |
| **Checkout - models.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d1fd7bbf-8c70-49be-81d3-22c06681884a) | No Errors  |
| **Checkout - signals.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/79d77527-478c-4997-8d00-11d250c6895d) | No Errors  |
| **Checkout - test_forms.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/626e677e-9a90-4683-a151-3ae857b83b12) | No Errors  |
| **Checkout - test_views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/3ea2dd4a-8b96-4c74-b0a0-f6077f38c69a) | No Errors  |
| **Checkout - urls.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/3577315e-612d-4a91-a5e4-e25d7009b7af) | No Errors  |
| **Checkout - views.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/eb348f8c-1205-4c09-9467-ac917a6ddc58) | No Errors  |
| **Checkout - webhook_handler.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/6d52c63a-7c19-4e82-bf36-4c0801977993) | No Errors  |
| **Checkout - webhooks.py** | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/636c94d3-2b3a-4eaa-bdf7-ccc765ed342a) | No Errors  |
| **Coaches - admin.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/cfda50fe-f21c-41a9-a933-182dfd5e66ef) | No Errors  |
| **Coaches - models.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/69857409-d2f4-416f-9023-37bf63d1a9e7) | No Errors  |
| **Coaches test_views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/204516a9-c86c-42d5-9993-2995ad802813) | No Errors  |
| **Coaches urls.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/05208b8a-d9ed-4b1f-9952-2ee71e6ef050) | No Errors  |
| **Coaches views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/5688f488-920b-42e2-b9fd-16476599475b) | No Errors  |
| **Courses - admin.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/24daa236-445c-4399-bd6e-1a13092c106e) | No Errors  |
| **Courses - forms.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/dedd37f0-e293-49fb-b44c-b0fca58e0114) | No Errors  |
| **Courses - models.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/3cc46026-767e-4b6a-a889-315e1384bbb4) | No Errors  |
| **Courses - test_forms.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e096e5cf-0b40-4669-9d9c-748cd1d19a08) | No Errors  |
| **Courses - test_views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/b869e84b-0b9a-4ef2-8258-292bb1f79f5b) | No Errors  |
| **Courses - urls.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/1ac67cac-12d2-4542-a239-7351bce42205) | No Errors  |
| **Courses - views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/c01dae35-9d25-489f-8183-d4f6265ab6f7) | No Errors  |
| **Home - test_views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d38b2731-af42-4701-8a69-9280a4531b9b) | No Errors  |
| **Home - urls.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e2e73b18-211c-4cfa-ad12-b5351cbd0a07) | No Errors  |
| **Home - views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d59ba79f-118d-4668-ac98-baacdb9caacb) | No Errors  |
| **Profiles - admin.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/36ea54ee-c45b-4785-ae3b-a5f1293116d1) | No Errors  |
| **Profiles - forms.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/be88e7bb-d7aa-4293-bf8d-4de9783f5d59) | No Errors  |
| **Profiles - models.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/b7aad2e0-5d33-492f-87c4-c65a095bfb1f) | No Errors  |
| **Profiles - test_forms.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/c0088223-a127-4173-8c8d-8f31d380caa8) | No Errors  |
| **Profiles - test_views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/52645bc8-a5c4-4459-a57a-1289e01a8979) | No Errors  |
| **Profiles - urls.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/168b0441-5fd6-44d9-b3e7-759e661d9c35) | No Errors  |
| **Profiles - views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/91890640-1ccd-47d1-a49f-9aac6117f683) | No Errors  |
| **Snapcallcoaching - settings.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d22c5855-194b-4dd4-85a6-8987c9ff7bd2) | No Errors  |
| **Snapcallcoaching - urls.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/85bb3f9f-32ea-4ee2-84f9-d027df96eef6) | No Errors  |
| **Snapcallcoaching - views.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/c48d5bae-fff2-4aa3-bf1e-a7ca14cca4b8) | No Errors  |
| **Snapcallcoaching - wsgi.py**         | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7210d872-eb9a-4543-96e8-4603951acbc2) | No Errors  |


## Accessibility
I confirmed the code used is accessible by using lighthouse in devtools. While initially there was a lower score for performance and accessibility I was able to improve these by minimising images and adding aria labels where appropriate. It was also necessary to change the font color of placeholder text.

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/01264a54-18ba-4e4c-bcb7-4e8885249d30)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/eb00dac5-2ab8-433e-9f1a-dcfcba18e3a8)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/067b018d-e7cb-431e-8ff2-9e8a3663c775)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e55cd2df-c975-4d81-ba06-786736b6de69)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/f9507614-216e-47a8-946f-27e21f090445)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/203803ef-6bdf-4d32-9779-16eae39e5557)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/10d1c651-5c32-4d84-ae37-5094a59b6f33)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7288e5a3-3c0f-4c00-8f8d-82328f10a310)

<img width="600" alt="image" src="https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/73b13d01-3a81-4c90-bfa9-e40adcff7668">

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9f15a3f3-6892-4ddd-bd13-328bc3d60a9a)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/2eb5945e-943e-4002-af3a-bb0d3ea44324)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/3d271be4-1e9f-4ca8-bac5-642a90397a8c)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/7d57c8c8-5afd-43b0-bc27-666e53a11058)

![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/0ffaaf6d-4db3-4959-8b14-6fc00295c291)















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
The site was tested and was confirmed to display correctly, be responsive and comatible with the following browsers:
- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/browsers/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge?ep=192&form=MA13L1&es=40)

# Device Testing
The site was tested and was confirmed to display correctly and be responsive on the following devices:
- Desktop Computer
- iPhone 14 Pro Max - during testing on this device it was discovered that the "My Account" drop-down menu was hidden behind the footer in the collapsed navbar view. This was fixed.
- Galaxy S8
- IPAD Pro

# Unit Testing
Due to time constraints limited unit testing has been carried out. This was done using Django's built in unit testing framework. After testing was complete I ran a coverage test and the results were as follows:
![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/42cb3983-9729-49aa-a55e-9fc0b7abf72d)

The tests carried out were as follows:

| File                 | Code                                      | 
| -------------------- | ------------------------------------------- | 
| [Bag Views](bag/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/e5400b0e-f897-4e35-80c7-e2d9f103b7be) |
| [Checkout Forms](checkout/test_forms.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/173cc1db-9754-47b3-beed-d994358a626a) |
| [Checkout Views](checkout/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/d053f765-04a4-41e5-af3e-ee59214d0e53) |
| [Coaches Views](coaches/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/ae5c67f7-1fe5-4a96-849b-ad160fd3c994) |
| [Courses Forms](courses/test_forms.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/23eaa7c7-1588-4594-91d4-2861e01b140a) |
| [Courses Views](courses/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/1101806c-c858-4ece-8b96-46b885aad1ab) |
| [Home Views](home/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/df98d0bf-0b69-4991-a40f-4c58e73aefd5) |
| [Profiles Forms](profiles/test_forms.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/9efe6346-e95a-4d42-8535-764e9a0ce0a4) |
| [Profiles Views](profiles/test_views.py) | ![image](https://github.com/tomkelly111/Snap-Call-Coaching/assets/111172617/333f34bd-9f37-4516-91c1-f9766bcf16e9) |


# Bugs
## Solved Bugs
See comments section of manual testing. 

## Remaining Bugs
None known.


end.
