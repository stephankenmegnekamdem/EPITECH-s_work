def count_cat(s):
 new_s = s.lower()
 word='cat'

 num_cat=0
 for j in range(2):
  count=0
  if j==1:
      new_s = new_s[::-1]

  for i in range (len(new_s)):

    if new_s[i]==word[0]:
      count=count+1
      continue

    if count==1:
      if new_s[i]==word[1]:
       count=count+1
       continue
      else:
       count=0
       continue

    if count==2:
      if new_s[i]==word[2]:
       num_cat=num_cat+1
       count=0
       continue
      else:
       count=0
       continue


 word = 'garden'


 for j in range(2):
      count = 0
      if j == 1:
          new_s = new_s[::-1]

      for i in range(len(new_s)):

          if new_s[i] == word[0]:
              count = count + 1
              continue

          if count == 1:
              if new_s[i] == word[1]:
                  count = count + 1
                  continue
              else:
                  count = 0
                  continue

          if count == 2:
              if new_s[i] == word[2]:
                  count = count + 1
                  continue
              else:
                  count = 0
                  continue

          if count == 3:
              if new_s[i] == word[3]:
                  count = count + 1
                  continue
              else:
                  count = 0
                  continue

          if count == 4:
              if new_s[i] == word[4]:
                  num_cat = num_cat + 1
                  count = 0
                  continue
              else:
                  count = 0
                  continue

 word = 'mice'


 for j in range(2):
     count = 0
     if j == 1:
         new_s = new_s[::-1]

     for i in range(len(new_s)):

         if new_s[i] == word[0]:
             count = count + 1
             continue

         if count == 1:
             if new_s[i] == word[1]:
                 count = count + 1
                 continue
             else:
                 count = 0
                 continue

         if count == 2:
             if new_s[i] == word[2]:
                 count = count + 1
                 continue
             else:
                 count = 0
                 continue


         if count == 3:
             if new_s[i] == word[3]:
                 num_cat = num_cat + 1
                 count = 0
                 continue
             else:
                 count = 0
                 continue
 print(num_cat)

s=input("Enter a sentence\n")
count_cat(s)
