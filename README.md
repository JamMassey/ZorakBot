# ZorakBot

ZorakBot is the House bot of the Practical Python discord server. Zorak is developed with features by the community. Anyone from our server can contribute. 


## User Commands
#### For-fun commands
- z.hello
- z.catfact
- z.dogfact
- z.pugfact
- z.quote
- z.joke
- z.8ball [question]
- z.taunt
- z.rolldice
- z.catpic
- z.dogpic [breed] (Optional)
- z.pokedex [pokemon]
#### Utility Commands
- z.google [question]
- z.embed [title] [ content ]  
- z.zeus [website]
- z.fakeperson
- z.userinfo/z.whois
- z.avatar/z.av
- z.ping
- z.pipsearch/z.pypi/z.pip [package]
- z.git/z.github [endpoint]
#### Admin Commands
- z.echo [message]
- z.rules [title] [rules]

## Deployment

Run 'pip install .' in the root directory to pull all dependencies and create a build of zorak_module. Build is then runnable via a call to  zorak_bot/__main__.py script.

If you're developing on the project you won't want to rebuild the module each time you make a change, so you can do this once to set up your enviroment and then delete the two generated build folders within zorak_module, before continuing to run __main__.py. Or alternitevely if using VSCode install the Jupyter extension and you can add '#%%' at the top of __main__.py (or anywhere for that matter) to run/debug as a Jupyter cell.

Optional arguments: 

| Parameter |   Long Parameter   |                                     Default                                     | Description                                               |
| :-------- | :----------------: | :-----------------------------------------------------------------------------: | :-------------------------------------------------------- |
| -h        |       --help       |                                                                                 | Show help message and exit program                        |
| -lf       |    --log_file      |                                      None                                       | .log file to output logs to. No output if left as default |
| -ef       |    --err_file      |                                      None                                       | .log file to output errs to. No output if left as default |
| -ll       |    --log-level     | INFO [(Enum 20)](https://docs.python.org/3/library/logging.html#logging-levels) | Logger level                                              |

Optional flags:

| True Flag     |    False Flag    | Default | Description                 |
| :------------ | :--------------: | :-----: | :-------------------------- |
| --console-log | --no-console-log |  True   | Flag for logging to console |
