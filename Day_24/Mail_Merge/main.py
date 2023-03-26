#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

sample_letter_file = r"C:\Without_Sync\Py\python-100-days\Day_24\Mail_Merge\Input\Letters\starting_letter.txt"
name_file = r"C:\Without_Sync\Py\python-100-days\Day_24\Mail_Merge\Input\Names\invited_names.txt"

with open(name_file) as namefile:
    unformatted_names=namefile.readlines()
    formatted_names = []
    #Way 1 : Remove \n from the names
    # for name in unformatted_names:
    #     corrected_name = name.replace("\n","")
    #     formatted_names.append(corrected_name)    
    #Way 2 : To strip the \n
    for name in unformatted_names:
        corrected_name = name.strip()
        formatted_names.append(corrected_name)
    print(formatted_names)

with open(sample_letter_file) as sample_letter:
    pre_letter=sample_letter.read()
    #print(pre_letter)
    # post_letter=pre_letter.replace("[name]",formatted_names[0])

#Creating mail for all names
for name in formatted_names:
    picked_name=name
    post_letter=pre_letter.replace("[name]",picked_name)
    #Saving the letters in ready to send
    send_path = r"C:\Without_Sync\Py\python-100-days\Day_24\Mail_Merge\Output\ReadyToSend" 
    with open(f"{send_path}\letter_for_{picked_name}.txt", mode="w") as new_email:
        new_email.write(post_letter)