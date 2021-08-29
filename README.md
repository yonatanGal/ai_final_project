# Instructions for running the code:

1. use git clone / download all our files to a repository in your local computer

2. open a terminal, get to the code repo, and install all relevant packages
   using the command:
   ```
   pip install -r requirements.txt
   ```

3. in order to run our code, you should follow the following format:
   ```
   python main.py --algorithm=x --style=y --tempertaure=z
   ```

   Parameters explanation:
   x varies from 1 to 3. 1 - CSP + Qlearner, 2 - CSP with best match,
   3 - CSP with random choice.

   y varies from 1 to 5. 1 - Home, 2 - Sport, 3 - Casual, 4 - Casual Elegant,
   5 - Formal.

   z varies from 0 to 35 degrees (in celsius).

   after running this command you'll get the best choice from out db, according
   to your chosen parameters. enjoy!


