from ctransformers import AutoModelForCausalLM
llm = AutoModelForCausalLM.from_pretrained('TheBloke/Llama-2-7B-Chat-GGML', model_file = 'llama-2-7b-chat.ggmlv3.q4_K_S.bin')
for word in llm('Write a joke on elon musk', stream = True):
  print(word, end= '')
