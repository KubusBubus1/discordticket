#--------Ticket-Bot Config File--------#
#Created by WebTheDev#

#PLACE THE TOKEN FOR THE BOT IN THE TOKEN.JSON FILE!!!!#

import json

#Main Config:#
botStatusType = 'Watching'                                                   #Bot Status Type (Ex. Playing, Watching, Listening, or Streaming)
botStatusMessage = 'Sprawuje Piecze nad ViceCity'                                                #The message that is shown on the bots activity
guildID = 1272649507330326629                                           #ID of the Guild the the bot is running in
ticketLogsChannelID = 1284622934379466914                                 #ID of the Channel to send system logs to
ticketTranscriptChannelID = 1284622851604742214                      #ID of the Channel to send ticket transcripts to
databaseName = 'tickets.db'                                          #Leave set to default value unless if you want to use a different database name
debugLogSendID = 839981909756739626                                     #ID of the Bot Owner to send debug information to

#Ticket Creation/Options Config:#
IDOfChannelToSendTicketCreationEmbed = 1284622671396737024               #ID of the Channel to send the Create a ticket embed to
IDofMessageForTicketCreation = 1284623614964138028                       #This variable was automatically adjusted.
activeTicketsCategoryID = 1284621227083694241                      #ID of the active tickets category
onHoldTicketsCategoryID = 1284622392102096946                             #ID of the onhold tickets category
archivedTicketsCategoryID = 1284622479469580480                    #ID of the archived tickets category

OptionsDict = {
    "Option 1": ("Odwołanie od Bana 🔨", "odwolanie", "Odwołaj się od Bana"),                                      #This is the ticket options dictionary. It defines the different types of tickets that users can create.
    "Option 2": ("Support ❓", "support", "Ogólnopojęty Support"),                                #A ticket option definition should look something like this:  
    "Option 3": ("Report ✋", "report", "Zgłoś Gracza!")                    #"Option #": ("Title of Option", "Type of Option", "Description of Option")
}                                                                                                             #Add a comma after every option definition except for the last one. 
                                                                                                              #If you only have one option then no comma is needed.
                                                                                                                 

channelPerms = {                                                                                          #This is the ticket channel perms dictionary.
    "odwolanie": (1272649507393241251, 1272649507393241252, 1272649507405959222, 1272649507405959223, 1272649507405959224, 1272649507405959225, 1272649507405959226, 1272649507405959227, 1272649507405959228, 1272649507405959229, 1272649507405959230, 1272649507405959231, 1272649507418538057),                                                                     #This dictionary defines what roles will have access to each type of Ticket Channel
    "support": (1272649507393241251, 1272649507393241252, 1272649507405959222, 1272649507405959223, 1272649507405959224, 1272649507405959225, 1272649507405959226, 1272649507405959227, 1272649507405959228, 1272649507405959229, 1272649507405959230, 1272649507405959231, 1272649507418538057),                                           #Each type can support multiple role IDS
    "report": (1272649507393241251, 1272649507393241252, 1272649507405959222, 1272649507405959223, 1272649507405959224, 1272649507405959225, 1272649507405959226, 1272649507405959227, 1272649507405959228, 1272649507405959229, 1272649507405959230, 1272649507405959231, 1272649507418538057)                                              #Each entry into the definition should look something like this:
}                                                                                                         #"Type of Option":(ROLEID1, ROLEID2)
                                                                                                          #Add a comma after every option definition except for the last one. 
                                                                                                          #If you only have one option then no comma is needed.
                                                                                                          #IMPORTANT: MAKE SURE THAT THE TYPE OF OPTION IS THE SAME AS THE TYPE OF OPTION THAT WAS
                                                                                                          #DEFINED IN THE TICKET OPTIONS DEFINITION
                                                                                                          #IF NOT, PERMISSIONS WILL NOT BE SET CORRECTLY AND THE BOT WILL NOT WORK RIGHT.


ticketTypeAllowedToCreatePrivateChannels = "staff"                         #Set this to be the type of option (roles) as defined in the ticket channel perms dictionary that can use the /create command.
multipleTicketsAllowed = False                                             #Set this to True if you would like members to be able to have multiple tickets open at once (otherwise set to False).
dmTicketCopies = True                                                      #Set this to True if you would like the bot to dm Ticket Creators transcript copies of their ticket.


#Embed Config:#
footerOfEmbeds = ''                                                        #Set a custom embed footer of all embedded messages here!
embedColor = 0xffffff                                                      #Set a custom hex color code for all embeds! Make sure to keep the 0x!


def get_token():                                                    
    tokenFile = open("./token.json")                                       #This definition pulls the token from the token.json file
    data = json.loads(tokenFile.read())                                    #Make sure to put your token in the token.json file where it says "PLACETOKENHERE"!                                     
    return (data['BotToken'])


firstRun = False               #This variable was automatically adjusted.



#Please create a new issue on github if you are having issues with using the bot or find any bugs!