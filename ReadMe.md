# DZG_Dict - Decentralized Zeit Geist Dictionary 
Document created: April 12, 2021 by Patrick LaChapelle  
Last updated: April 12, 2021 by Patrick LaChapelle  
---
## Overview
The purpose of this project is to create a "living" dictionary - one in which anyone with an email address can add their own definition. Currently, the only open dictionaries that I can find require extensive review from editors. This dictionary will allow users to submit definitions for any word, from any language, and without any review whatsoever. The interface will be similar to reddit, where users will be able to upvote or downvote definitions. Also like reddit, users will be free to create sub-dictionaries, which can then be moderated. 
These subdictionaries are infinitely divisible into further sub-dictionaries, in the same way that classes are infinitely divisible into further sub-classes in object-oriented programming. For instance, one might have dictionary *Elementary-level reading English dictionary*, which is a subdictionary of *English Dictionary - profanity free*, which is a subdictionary of *English Dictionary*... so on and so forth, one gets the idea.  

## Project Plan  
Below, I lay out a brief overview of the plan as it currently stands.  
  
### Creating Github repository
The first and most obvious step in setting up this project is setting up a Github repository, where all of the definitions can be held. Ultimately, the project will need to move to a solution that has more data storage capabilities, as well as dynamic backend capabilities for the User Interfaces and the features that they will implement. In its simplest form, this repository will contain templates, definitions, and dictionary relationships exclusively, organized in some coherent structure.

### Building the bare-bones Desktop & Mobile Applications
Once there is a Github repository in place, there needs to be some simple mobile and desktop interfaces where users can easily contribute words without having to understand Git or the underlying data structures (making this accessible for non-coders).

### Adding Dynamic interface
The main feature of this site is the up/down voting, which is intended to filter out imprecise and poorly-worded definitions, as well as profane or non-existent words. This interface must also require the tracking of users, as well as some sort of verification that prevents things like bots posting incessantly, or spamming up/down likes. While the site does have to watch out for these sort of things, primarily for the purpose of limiting data (imagine some high number of bots that incessantly post made-up words), there is no need to monitor what *people* post, which I hope will simplify the requirements of this project.

### Funding Strategy
Once this projects incorporates dynamic features, we will have to figure out how to make money in a scalable way so that we can pay for the API. I have no intentions of making money, so the site only needs to pay for the hosting/API services. 

### Online site
With enough funding, this project should eventually be able to move onto a dynamic website - at which point I think it will be able to grow substantially. Like any collaborative project, this will require a high number of users for the site to function as intended.  

## Project Components  

In this section I detail some of the important components of this project, along with descriptions of appropriate requirements. 

### Sub-dictionaries
Of course, there must be some logical structure to our sub-dictionaries. The structure should be efficient and minimalist in design to optimize scalability, as the infinite divisibility of sub-dictionaries is a key component to this system.
