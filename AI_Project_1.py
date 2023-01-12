from pickle import FALSE, TRUE
import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words = []):
    message_certainty = 0
    has_required_words = True
    

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #to calculate the percentage of recognised words in user_message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response,list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #response-----------------------------------------------------
    response('Hello!', ['hello','hi', 'whats poppin', 'wassup','hey','whats the word','heyo','yo wassup'], single_response=TRUE)
    response('I\'m doing fine, and you?', ['hows it going?','how', 'are', 'you', 'doing'], required_words=['how'])
    response('I speak Igbo and english with a little bit of french',['what language','language','tongue','speak'],single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('That\'s great to know!', ['same', 'i\'m doing fine'],required_words=['same'])
    response('Thank you!',['i','love','cool'], single_response=True)
    response('Yea i\'m up late',['awake','up late'], single_response=True)
    response('Jammin music',['wyd',], single_response=True)
    response('whats funny :( ',['lmao','lol'], single_response=True)
    response('Its ok :)',['apologise','sorry'], single_response=True)
    response('I love it!',['sound','music'], single_response=True)
    response('Akward',['uhh','sooo','idk'], single_response=True)
    response(long.R_KNOWING, ['what does this mean?','tell me','answers','predict the future'],single_response=True)

    best_match=max(highest_prob_list, key=highest_prob_list.get)
    #the comment below is a code saved for later
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

    #testing response system
while True:
    print('Bot: ' + get_response(input('you: ')))
