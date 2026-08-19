class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += (str(len(i)) + "$" + str(i))
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_list = []
        l = len(s)
        i=0

        word_l = ""
        
        while(i<len(s)):
            dec_str = ""
            i_val = s[i]
            if(i_val != "$"):
                word_l += s[i] 
                i += 1
            if(i_val == "$"):
                word_l = int(word_l)
                dec_str = s[i+1: i+word_l+1]
                decoded_list += [dec_str]
                i = i+word_l+1
                word_l = ""
                

            # print("length:",l)
            # print("i:",i)
            # # if(s[i+1] == "$"):
            # start_index = i+2
            # end_index = int(s[i])+ start_index
            # if(s[i] == "0"):
            #     word = ""
            # else:
            #     print(start_index,end_index)
            #     word = s[start_index:end_index]
            # decoded_list += [word]
            # print(decoded_list)
                
            # i = end_index
            
            
    
        return decoded_list