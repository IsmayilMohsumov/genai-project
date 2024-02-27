from openai import OpenAI
import os
client = OpenAI()

key = os.environ.get('OPENAI_API_KEY')
client.api_key = key


# function to write file  
def write_content_to_file(content, file_path):
    file_path_root = 'C:\\Users\\mohsu\\Downloads\\GEN AI\\Pandora\\genai-pandora\\dataset\\' + file_path
    with open(file_path_root, 'w') as file:
        file.write(content)
    print(f'The content has been successfully written to {file_path_root}')

# function to read from file
def read_from_file(file_path):
    file_path_root = 'C:\\Users\\mohsu\\Downloads\\GEN AI\\Pandora\\genai-pandora\\dataset\\' + file_path
    with open(file_path_root, 'r') as file:
        file_content = file.read()
    return file_content
    




# 1 - Describe image and write to file
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the image by extracting the SAP form elements, their roles and any additional information"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://lh3.googleusercontent.com/drive-viewer/AEYmBYQAXEdjs4N66v_9QIg5VFViTEViPAHCZTfBhZJKfQOmb9DeZ2i0nUPaVG1lyyMUKlTKlQLoxBBe10fBOOU1e-Ua_xyK7w=w1920-h878",
                    },
                },
            ]
        }
    ],
    max_tokens=300,

)
print(response.choices[0].message.content)
write_content_to_file(response.choices[0].message.content, '1_sap_description.txt')




# 1 - Reading from file and developing functional specification and write to file
print("-------------------- Developing functional specification... ------------------")
response_content = read_from_file('sap_description.txt')
messages = [
    {"role": "system", "content": "You are a SAP business analyst. Develop functional specification for the given input"},
    {"role": "user", "content": response_content}
]

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=messages
)

print(response.choices[0].message.content)
write_content_to_file(response.choices[0].message.content, '2_func_spec.txt')









# 1 - Reading from file and developing testcases and write to file
file_content = read_from_file('2_func_spec.txt')
print(file_content)

messages = [
    {"role": "system", "content": "You are a SAP tester. Develop testcases for the given functional specification. Test cases should have testcase_id, description, steps and etc."},
    {"role": "user", "content": file_content}
]

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=messages
)

print(response.choices[0].message.content)
write_content_to_file(response.choices[0].message.content, '3_testcases.txt')
