'''An example to show how to set up an pommerman game programmatically'''
import pommerman
import torch
from pommerman import agents

import pygame
import pygame_menu

import webbrowser

### Menu Configurations
COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (15 * TILE_SIZE, 15 * TILE_SIZE)

clock = None
surface = pygame.display.set_mode(WINDOW_SIZE)

def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)
###

#Pre Game menu
def pre_game_menu_loop():
    pygame.init()

    pygame.display.set_caption('Pommerman.io Pre Game')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=int(TILE_SIZE*0.8),
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
        widget_shadow=False
    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.9),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play menu'
    )



    information_participation_sheet_and_consent_form = """You are being invited to take part in research on machine learning implementations in game AI.
    Denzel Guma, student at Coventry University is leading this research. Before you decide to take part, it is
    important you understand why the research is being conducted and what it will involve. Please take the time to read the following information carefully

    What is the purpose of this research?
    The purpose of the research is to show whether machine learning techniques can be effectively applied to game AI development to produce AI that can mimic human behaviour

    Who is organising and funding the research? 
    The research is being organised and funded by Coventry University. The research was granted ethical approval by Coventry University’s Research Ethics Committee P130897. 

    Do you have to take part?
    No – it is entirely up to you. If you do decide to take part, please keep this Information Sheet and complete the Consent Form to show that you understand your
    rights in relation to the research, and that you are happy to participate. Please note down your participant number and provide this to the lead researcher if you wish to
    withdraw from the research later. You are free to withdraw your information from the research at any time until the data is destroyed on 1/8/22. You do not need to provide a
    reason for withdrawing. A decision to withdraw, or not to take part, will not affect you in any way.

    What will happen if I decide to take part?
    You will be asked to join a game session on Itch.IO and play a game of bomber man. Once you finished the game session you will be asked a series of questions. The questionnaire
    will take place within once the game session has finished. It should take around 1-3 mins and I would like to a collect and store your response on a secure server 

    Why have you been invited to take part? 
    You have been invited to participate in this research because you are a Coventry University student or a member of the general public

    What are the benefits and potential risks and benefits in taking part?
    By taking part, you will be helping Denzel Guma and Coventry University to better understand the effectiveness of machine learning implementation within video game AI development.
    There are no significant risks associated with participation.

    What information is being collected in the research? 
    Your IP address and your qualitative response are being collected through this research. 

    Lawful basis of processing 
    Under the UK General Data Protection Regulation (UK GDPR) 2016 we must have a lawful basis to process your personal data and for the purpose of this research, our lawful basis is
    that of consent. 

    What will happen to the results of the research?
    The results of this research may be summarised in published articles, reports, and presentations. Quotes or key findings will always be made anonymous in any formal outputs unless
    we have your prior and explicit written permission to attribute them to you by name 

    Who will have access to the information?
    Your data will only be accessed by the researcher/research team. 

    Where will the information be stored and how long will it be kept for?
    Your data will be processed in accordance with the UK General Data Protection Regulation 2016 (UK GDPR) and the Data Protection Act 2018 (DPA). All information collected about you
    will be kept strictly confidential. Unless they are fully anonymised in our records. 
    All electronic data will be stored on a Secure Local Server and Coventry University OneDrive. Your consent information will be kept separately from your responses. The researcher
    will take responsibility for data destruction and all collected data will be destroyed on or before 1/8/22
    For further information about how Coventry University will handle your personal data, please read our Privacy Notice for Research Participants. 

    What will happen next?
    If you would like to take part, complete the consent form indicating that you will be a willing participant 

    Researcher contact details:
    Denzel Guma , gumad@uni.coventry.ac.uk 
    YingLiang Ma , ac7020@coventry.ac.uk  

    Who do I contact if I have any questions or concerns about this research?
    If you have any questions, or concerns about this research, please contact the researcher, or their supervisor. If you still have concerns and wish to make a complaint, please
    contact the University’s Research Ethics and Integrity Manager by e-mailing ethics.uni@coventry.ac.uk. Please provide information about the research project, specify the name
    of the researcher and detail the nature of your complaint.

    Consent Form Agreements:
    I confirm that I have read and understood the Participant Information Sheet for the above research project and have had the opportunity to ask questions.
    I understand that all the information I provide will be held securely and treated confidentially. I understand who will have access to any personal data provided and
    what will happened to the data at the end of the research project.
    I understand my participation is voluntary and that I am free to withdraw my participation and data, without giving a reason, by contacting the lead at any time
    until the date specified in the Participant Information Sheet.
    I understand the results of this research will be used in academic papers and other formal research outputs.

    
    Thank you for taking time to read this information sheet and accepting the consent form aggreements.
    """

    play_menu.add_label(information_participation_sheet_and_consent_form, max_char=65, font_size=15)

    play_menu.add_button('Play and Connect to A Server',
                         run_game)

    play_menu.add_button('Return  to  main  menu', pygame_menu.events.BACK)

    how_to_play_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.4),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
        widget_shadow=False
    )

    how_to_play_menu = pygame_menu.Menu(theme=how_to_play_menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.7),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='How to Play'
    )
    how_to_play_menu.add_label("Player Controls: ")
    how_to_play_menu.add_label("Movement: WASD")
    how_to_play_menu.add_label("Plant bomb: E")

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.6),
        width=int(WINDOW_SIZE[0] * 0.6),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Pre Game Main menu'
    )

    main_menu.add_button('Play', play_menu)
    main_menu.add_button('How to Play', how_to_play_menu)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
    while True:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        main_menu.mainloop(surface, main_background, disable_loop=False, fps_limit=0)
        main_menu.update(events)
        main_menu.draw(surface)

        pygame.display.flip()


#Post Game menu
def post_game_menu_loop():
    pygame.init()

    pygame.display.set_caption('Pommerman.io Post Game')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=int(TILE_SIZE*0.8),
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
        widget_shadow=False
    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.7),
        width=int(WINDOW_SIZE[0] * 0.9),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play menu'
    )

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * 0.6),
        width=int(WINDOW_SIZE[0] * 0.6),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Post Game Main menu'
    )

    main_menu.add_button('Play Again', run_game)
    main_menu.add_button('Answer Questionaire', url_direct_to_questionaire)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
    while True:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        main_menu.mainloop(surface, main_background, disable_loop=False, fps_limit=0)
        main_menu.update(events)
        main_menu.draw(surface)

        pygame.display.flip()


def url_direct_to_questionaire():
    webbrowser.open('https://forms.office.com/r/CpTww4BfdK')

def run_game():
    '''Simple function to bootstrap a game.
       
       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    print(pommerman.REGISTRY)
    
    model = agents.A3CNet()#A3C model 
    model.load_state_dict(torch.load('.\A3C_v10_cnn_lstm_trained_critic_actor_1.pth'),strict=False)# Loading Trained A3C model

    # Create a set of agents (exactly four)
    agent_list = [  
        agents.A3CAgent(model), #top left
        agents.RandomAgent(),   #bottom left
        agents.SimpleAgent(),   #bottom right
        agents.PlayerAgent(agent_control="wasd"),# top right
        # agents.DockerAgent("pommerman/simple-agent", port=12345),
    ]
    # Make the "Free-For-All" environment using the agent list
    env = pommerman.make('PommeFFACompetition-v0', agent_list)

    # Run the episodes just like OpenAI Gym
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            env.render()
            actions = env.act(state)
            state, reward, done, info = env.step(actions)
        print('Episode {} finished'.format(i_episode))
    env.close()
    post_game_menu_loop()
    

def main():
    pre_game_menu_loop()
    #run_game()


if __name__ == '__main__':
    main()
