# Django_Fundamentals

Fundamental_Django_For_Medics

Basically it took me a while to get my head around django. These are all the django projects and apps I had to build before I understood how to build the backend using django. mysite was built by watching a YouTube video but to be honest I didn't understand it until I took an Udemy course which forced me to keep repeating all the actions until it stuck!

Basically there is settings.py which controls everything and interacts with the django admin (which is a bit like an early backend of wordpress or something like that.

Then urls.py tells everyone else where all the sites consitutent parts are. Then you need to connect an app and by using the render function get views.py to communicate with a urls.py file inside the app in order to keep everything neat and modular and these need to be configured.

Then you use views.py to instruct the creation of models within the app. Models.py can then use the django models to create user objects or whatever objects you need within your app. You can then migrate these to the backend which is a sqlite3 engine by default. 

Then you can create the django superuser from within admin.py using admin.site.register(User). This can be used to inspect the databases visually, but you have to keep it secure.

You can then use a script to populate the database with test data which I did in the first couple of projects to make sure everything was working ok - see the populate_users in the third_project for an idea of this.

Then by this point project I started playing around with forms and then, revisited the third project to try storing the input of the forms to the database and that worked fine. I also played around with adding fields to stop bots and ensure that the input was clean.

Then on the fourth project I started exploring templating and then finally logins. Django is awesome!

Then the 5th project covers more advanced templating.

The 6th is all about user login forms and the logic behind them.

After that I started actually deploying projects. This concludes the basic_Django_training repo.
