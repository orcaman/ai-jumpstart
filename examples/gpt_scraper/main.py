from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import openai


def get_chat_completion(
        messages,
):
    """
    Generate a chat completion using OpenAI's chat completion API.
    Args:
        messages: The list of messages in the chat history.
        engine: The name of the model to use for the completion. Default is gpt-3.5-turbo, which is a fast, cheap and versatile model. Use gpt-4 for higher quality but slower results.
    Returns:
        A string containing the chat completion.
    Raises:
        Exception: If the OpenAI API call fails.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    choices = response["choices"]  # type: ignore
    c = choices[0].message.content.strip()
    return c


# main function to run the script
if __name__ == "__main__":
    m = [{
        "role": "system",
        "content": """Extract the Location, Asset Class, Year Built, Units and JPG Image from the HTML page who's 
        content is provided by the user, do not include line breaks"""
    }, {
        "role": "user",
        # "content is an html string with a list that contains location, asset class, year built, units and jpg image"
        "content": """<div class="property-detail">
        <div class="property-detail__header">
            <div class="property-detail__header__title">
                <h1>Property Details</h1>
            </div>
        </div>
        <div class="property-detail__body">
            <div class="property-detail__body__content">
                <div class="property-detail__body__content__section">
                    <div class="property-detail__body__content__section__title">
                        <h2>Location</h2>
                    </div>
                    <div class="property-detail__body__content__section__content">
                        <p>123 Main Street, San Francisco, CA 94105</p>
                    </div>
                </div>
                <div class="property-detail__body__content__section">
                    <div class="property-detail__body__content__section__title">
                        <h2>Asset Class</h2>
                    </div>
                    <div class="property-detail__body__content__section__content">
                        <p>Office</p>
                    </div>
                </div>
                <div class="property-detail__body__content__section">
                    <div class="property-detail__body__content__section__title">
                        <h2>Year Built</h2>
                    </div>
                    <div class="property-detail__body__content__section__content">
                        <p>2000</p>
                    </div>
                </div>
                <div class="property-detail__body__content__section">
                    <div class="property-detail__body__content__section__title">
                        <h2>Units</h2>
                    </div>
                    <div class="property-detail__body__content__section__content">
                        <p>100</p>
                    </div>
                </div>
                <div class="property-detail__body__content__section">
                    <div class="property-detail__body__content__section__title">
                        <h2>Image</h2>
                    </div>
                    <div class="property-detail__body__content__section__content">
                        <img src="https://www.example.com/image.jpg" />
                    </div>
                </div>
            </div>
        </div>
    </div>"""
    }]

    completion = get_chat_completion(m)
    print(completion)
