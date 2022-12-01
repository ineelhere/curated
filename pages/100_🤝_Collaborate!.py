import streamlit as st
from custom_functions import *

display_banner()
display_logo()

st.header('CURATED | Collaborate! 🤗 ')

st.markdown('''
**Curated** aims to assist individuals learning new technical skills
with a proper, well researched, community driven reference point to keep them
**well informed** about several awesome resources which they might find immensely useful in their journeys. In simple terms, the aim is not to teach. The aim is just to keep folks **informed**.

Now, creating such a project demands collective knowledge, skills and expertise. 
This is where you, as an open source contributor, can help!

#### Collaborations are always welcome. 
* Check the developmental version of the webapp - https://curated-dev.streamlit.app/ . Your contribution shall reflect on this release first.
* Just raise an issue or create a PR on the `development` branch - https://github.com/ineelhere/curated/tree/development with your code<br>
* Once your PRs are reviewed and merged, all developmental releases can be seen/tested here https://curated-dev.streamlit.app/ <br>
* Once everything looks fine, the developments shall be moved to the main webapp at https://curated.streamlit.app/

![](https://i.imgur.com/fPVyfoI.gif)
<br><br>
Just kidding. Please let me know your feedback and suggestions :)


<br>Let this become an awesome crowd-sourced repository to know about awesome resources for learning new skills.
<br>Have fun! 



''', unsafe_allow_html=True)



footer()