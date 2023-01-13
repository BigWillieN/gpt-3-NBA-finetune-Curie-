Objective: Create a simple AI Model that can answer your questions based on 2019-2020 NBA Player statistics.
Method: Fine tuning the GPT-3 Engine to create a model that fits our use.
Steps: To fine-tune ChatGPT using the OpenAI CLI, you will need to first prepare your training data in the format of a JSONL file, where each line is a prompt-completion pair. 
You can use Kaggle to find data sets that fit your purpose. Next, you will need to install the OpenAI CLI on your editor/cmd.
You can then use that to create a fine-tuned model, using the training data file and the base model of your choice (ada, babbage, curie, or davinci).
Once the fine-tuning job has succeeded, you can use the fine-tuned model name as the model parameter of a completion request using the OpenAI CLI, cURL, Python, or Node.js.
That should be all. But if you want a simple GUI Interface to interact with your AI Model, you can use my code to create that as well.
