import json
import os
import streamlit as st
from requests import request


class Article():
    def __init__(self, title, source, url, content, publication_date):
        self.title = title
        self.source = source
        self.url = url
        self.content = content
        self.publication_date = publication_date


def display_articles():
    st.title('AI News Aggregator')
    tab1, tab2 = st.tabs(["Aggregated News", "Add a newsletter"])
    with tab1:
        st.header('Aggregated AI News')
        url = 'http://localhost:8000/data'
        response = request('GET', url)
        response.raise_for_status()
        articles = json.loads(response.text)
        print(articles)
        for article in articles:
            st.subheader(article['fields']['title'])
            st.write(f"Source: {article['fields']['source']}")
            st.write(article['fields']['content'])
            st.write(f"[Read more]({article['fields']['url']})")
            st.write("---")
    with tab2:
        st.subheader("Add a new Newsletter")
        # name = st.text_input("Name")
        with st.form(key='Newsletter'):
            st.write('Newsletter')

            title = st.text_input(label="Title")
            url = st.text_input(label="Url")

            submit_form = st.form_submit_button(label="Add", help="Click to Add!")

            # Checking if all the fields are non empty
            if submit_form:
                st.write(submit_form)

                if url and title:
                    # add_user_info(id, name, age, email, phone, gender)
                    st.success(
                        f"ID:  \n url: {url}  \n title: {title}"
                    )
                    request(method='GET', url=f'http://localhost:8000/data/addLetter?title={title}&url={url}')
                else:
                    st.warning("Please fill all the fields")


if __name__ == "__main__":
    display_articles()
