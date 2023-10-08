import gradio as gr

## Gradio dashboard code.
### Allows user to upload Notion directory zip file.
### Provide the Open AI API.
### QnA with Notion bot.


def create_bot_ui(api_key_return_fn, notiondb_file_return_fn,
                  input_prompt_return_fn):
  with gr.Blocks() as notion_bot_ui:
    gr.Markdown("# Say Hello to Notion AI Assistant!")
    gr.Markdown("## I am a QnA bot over your uploaded Notion database")

    # Pass the OpenAI API key.
    gr.Markdown("### Step 1 : Provide the Open AI API key. ")
    openai_api_key_ct = gr.Textbox(
        placeholder="Provide OpenAI API key. Press Enter.", type="password")
    openai_api_key_ct.submit(fn=api_key_return_fn, inputs=openai_api_key_ct)

    # Upload the Notion dashboard file.
    gr.Markdown("### Step 2 : Upload your Notion Database File.")
    file_upload_ct = gr.File(file_count='single',
                             file_types=[".zip"],
                             label="Upload Notion database as a zip file")
    file_upload_ct.upload(fn=notiondb_file_return_fn, inputs=file_upload_ct)

    # QnA UI.
    gr.Markdown("### Step 3 : Enter your prompt.")
    gr.Interface(fn=input_prompt_return_fn, inputs="text", outputs="text")
  return notion_bot_ui
