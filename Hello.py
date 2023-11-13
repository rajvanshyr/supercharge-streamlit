# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Raghav's Portfolio Site!! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Raghav is a generative AI developer who is passionate about helping buisnesses implement use cases
        **👈 Select a demo from the sidebar** to see some examples
        of what I've built
        ### Want to get in touch?
        - I can build you a custom website or GPT https://72hq44eclv8.typeform.com/to/dxvjvmt8
        - Check out my Medium Article https://medium.com/@rajvanshyr/supercharge-your-automated-customer-support-with-large-language-models-f0743e089ea2

    """
    )


if __name__ == "__main__":
    run()
