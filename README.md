# woz: an understanding initiative

Basically, this is a dashboard to send commands and monitor a remote interactive system and its virtual counterpart.

We are confined to a single party use case. Here is the background context for this application:

##  Wizard-of-Oz for Robotic Experiments

The goal here is to develop a modular wizard interface

In most of human-robot interaction experiments the robot is not fully autonomous. 
In these cases, the investigator becomes the puppeteer, or Wizard, 
and controls the robot without letting the participants of the experiment realise 
that the robot is merely remote controlled. 

The wizard can control all the functionalities of the robot 
or take over from the robot only in specific circumstances. 
This is usually done for safety reasons or because, 
when the variables under observation are all human-dependent, 
it is much more important that the experiment carries 
on without any interruption caused by a robotic malfunctioning. 
To be able to remote control the robot,
the wizard needs to have a full picture of what is happening in the experiment room 
in terms of flow of interaction between the robot and the participant, inner state of the robot, possible next action to take etc. 
The aim of the project will be to create a modular wizard interface, 
possibly integrating ROS, that could be easily used under different experimental conditions.

---

## Open Tasks

[ ] Must merge 1.py and 2.py such that buttons for gesture triggers send into the conversation. 
We are aiming for a conversation chess wherein the user realizes the system understands their state and intent.

[ ] For dialogue suggestions pane, try OpenAI/Claude/DeepSeek and as graceful fallback, a local LLM tuned for the specific task.

[ ] Replace the dummy analysis graph with perhaps, a live SER spectrograph (I have one built, will upload as soon as I find it)

[ ] Generally, make sense of what's going on with special emphasis to the real time realtime multimedia and audiovisual stream.

---
