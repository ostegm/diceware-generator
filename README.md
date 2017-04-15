# diceware-generator

This is a simple python script to allow a user to generate a random passphrase using the [diceware list of words](http://world.std.com/~reinhold/diceware.html). 
For more info on personal internet security checkout a [great post on Medium](
https://medium.com/@skeller88/personal-internet-security-how-to-avoid-getting-hacked-fdbcfeaa6cc4). 

### Note on Security
- It would probably be better to buy some dice and do this offline since you might have already been hacked and your new radomly generated passphrase was just logged to your bash history...
- But I'm lazy and dont have 6 dice....


### Usage
- Run the script with no arguments to get a random 8 word phrase
- Pass the --numwords or -n argument to change the length of your passphrase
- example: 
```    
python diceware-generator.py -n 4
```
