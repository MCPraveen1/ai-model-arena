import gradio as gr
from arena import battle

with gr.Blocks() as demo:

    gr.Markdown("# ⚔️ AI Model Arena")
    gr.Markdown(
        "Compare responses from Llama 3.3 70B and Llama 4 Scout."
    )

    prompt = gr.Textbox(
        label="Ask a Question",
        lines=3,
        placeholder="Type your question here..."
    )

    submit_btn = gr.Button("Submit")

    with gr.Row():

        with gr.Column():
            gr.Markdown("## Llama 3.3 70B")
            output1 = gr.Markdown()

        with gr.Column():
            gr.Markdown("## Llama 4 Scout")
            output2 = gr.Markdown()

    submit_btn.click(
        fn=battle,
        inputs=prompt,
        outputs=[output1, output2]
    )

demo.launch()