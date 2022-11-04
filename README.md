# TicTacToe - AI project

### Table of Contents  
* [Introduction](#Introduction)
* [Objectives](#Objectives)  
* [Main concept](#Main-concept) 
* [Problem and its formulation](#Problem-and-its-formulation) 
* [Game Tree](#Game-Tree) 
* [Minimax Algorithm](#Minimax=Algorithm) 
* [Alpha-Beta Algorithm](#Alpha-Beta-Algorithm)
* [GUI](#GUI)
* [Arabic virsion](#Arabic-virsion)
<a name="headers"/>


## **Introduction:**

This project covers a description and solution to the problem of the Tic-Tac-Toe game and its implementation with the best algorithm to apply the rules of the game and provide the best methods to ensure victory. 



## **Objectives:**

* Applying the principles of Minimax and Alpha-Beta. 

* Understand the distinctions between the Minimax and the Alpha-Beta algorithms in order to select the optimum algorithm. 

* Delivering the game in the most efficient structure and with the optimization technique possible, which reduces the search for the ideal position that leads to win. 

* Instead of dealing with codes, provide the game via entertaining interfaces that enable the reader to explore the game in a useful way. 



## **Main concept:** 

Tic-Tac-Toe is a game in which two players alternately place X and O in compartments spaced in a 3×3 grid, and each player tries to get a row of three X or three O (horizontal, vertical, or diagonal) before the opponent to win. If no one wins, then it is said to be a tie. The major idea is the development of the game using the alpha-beta algorithm to get the best game results. 



## **Problem and its formulation:**

### Problem: 

Developing an artificial intelligence that considers all alternatives and chooses the best positions to compete so that it always wins or draws and with the shortest time and space complexity. 

### Formulation: 

In artificial intelligence and game theory, we encounter search problems that can be interpreted by a graph of interconnected nodes, each representing a possible state. An intelligent agent must traverse graphs by evaluating each node to reach an optimal state.

Every AI move is based on the final output. If we want to create an AI that never loses, it might end up tied but never lose. So AI has to search from the available moves, which can lead to the best result (a win or even a tie). Nevertheless, there are specificific problems where standard graph search algorithms cannot be applied.
  
## Game Tree
  ![This is an image](https://telegra.ph/file/ec68273627be3637a2bfc.png)
  
  
## Minimax Algorithm

Minimax is a type of artificial intelligence that is used in two-player games like tic-tac-toe, checkers, chess, and go. This type of game is known as a "zero-sum game" because, in a mathematical representation, one player wins (+1) and the other loses (-1) or neither player wins (0).  

### Minimax Pseudocode
<img width="500" alt="Screen Shot 2022-11-04 at 12 51 12 PM" src="https://user-images.githubusercontent.com/75557453/199946436-113ae3e6-4cbf-4a26-8c87-890d907ae3dd.png">


### Minimax Example 
<img width="500" alt="Screen Shot 2022-11-04 at 1 06 35 PM" src="https://user-images.githubusercontent.com/75557453/199947289-c0933d12-18aa-4949-9862-9269dc692b42.png">

  
## Alpha-Beta Algorithm 

Alpha-beta pruning is a search strategy that seeks to minimize the number of nodes in the search tree that are evaluated by the minimax algorithm. It is an adversarial search algorithm that is commonly employed in two-player games for machine play. It stops examining a move when at least one alternative that proves the move is worse than a previously discovered option has been found.

### Alpha-Beta Pseudocode
<img width="500" alt="Screen Shot 2022-11-04 at 1 00 34 PM" src="https://user-images.githubusercontent.com/75557453/199946489-ea8f8ed0-9c4f-4199-a7d1-24461fefcda5.png">

### Alpha-Beta Example
 
  <img width="500" alt="Screen Shot 2022-11-04 at 1 06 47 PM" src="https://user-images.githubusercontent.com/75557453/199947380-596ead8a-3afe-4948-9fbc-407265dd9eed.png">


## GUI

<img width="200" alt="main" src="https://user-images.githubusercontent.com/75557453/199968883-313c8bf9-5af8-4b4e-99a0-61f7d6cc39a4.png">
<img width="200" alt="alphaBeta" src="https://user-images.githubusercontent.com/75557453/199968342-1b017f7f-d8a2-470f-8676-17e6d641d492.png">
<img width="200" alt="minimax" src="https://user-images.githubusercontent.com/75557453/199968356-764c9c0c-e3f5-4614-9841-938ec8388c5f.png">
<img width="200" alt="board" src="https://user-images.githubusercontent.com/75557453/199968362-9a166324-9d25-4fdd-8174-7518f9e9abc2.png">
<img width="200" alt="lose" src="https://user-images.githubusercontent.com/75557453/199968365-d8cea975-e2af-4615-b6b6-5e4b0d7ec1eb.png">
<img width="200" alt="tie" src="https://user-images.githubusercontent.com/75557453/199968369-ce9d583f-0252-4e67-9a91-531d9df932b2.png">
<img width="200" alt="win" src="https://user-images.githubusercontent.com/75557453/199968373-f70838d5-eec1-4b81-8712-2c6c8400eb30.png">



## Araic virsion
## تيك - تاك - تو

## المقدمة 

يغطي هذا المشروع وصفًا وحلًا لمشكلة لعبة Tic-Tac-Toe وتنفيذها بأفضل خوارزمية لتطبيق قواعد اللعبة وتقديم أفضل الطرق لضمان الفوز.


## الأهداف: 

تطبيق مفاهيم خوارزميات الميني ماكس والالفا بيتا بشكل عملي. 

فهم الفروقات بين الميني ماكس والالفا بيتا لمعرفة الخوارزمية الأفضل. 

توجيه القارئ لتحقيق افضل فهم للخوارزميتين. 

تقديم اللعبة في افضل صورة ومع افضل خوارزمية تختصر البحث عن الموضع الأفضل المؤدي الى الفوز. 

تقديم اللعبة في واجهات ممتعه بحيث تسهل على القارئ تجربه اللعبة بطريقه عمليه بدل من التعامل مع الاكواد. 


## المفهوم الرئيسي: 

تيك تاك تو هي لعبة يقوم فيها لاعبان بوضع X و O بالتناوب في مقصورات مقسمة  في شبكة 3 × 3 ، ويحاول كل لاعب الحصول على صف من ثلاثة X أو ثلاثة O (أفقيًا، رأسيًا أو قطريًا) قبل الخصم للفوز. إذا لم يفُز أحد ، تنتهي اللعبة بتعادل. 

والفكرة الرئيسية هي تطوير اللعبة باستخدام خوارزمية ألفا-بيتا للحصول على أفضل نتائج اللعب. 


## المشكلة وصياغتها: 

### المشكلة: 

بناء ذكاء اصطناعي يبحث في كل الاحتمالات الممكنة ويختار افضل مواضع اللعب بحيث يفوز دائما او يتعادل على الأقل وب اقل تعقيد للوقت والمساحة. 

### صياغة المشكلة: 

في الذكاء الاصطناعي ونظرية الألعاب، نواجه مشاكل بحث يمكن تطبيقها من خلال رسم بياني للعقد المترابطة ، كلٌ منها يمثل حالة محتملة. يجب على النائب الذكي عبور الرسوم البيانية من خلال تقييم كل عقدة للوصول إلى الحالة المثلى. 

تعتمد كل حركة يقدمها النائب الذكي على الناتج النهائية، حيث نريد إنشاء نائب ذكي لا يخسر أبدًا ، فقد ينتهي به الأمر متعادلًا ولكنه لا يخسر أبدًا. لذلك يتعين على النائب الذكي البحث في كل الحركات المتاحة، والتي يمكن أن تؤدي إلى أفضل نتيجة (الفوز أو حتى التعادل). ومع ذلك، هناك مشاكل محددة حيث لا يمكن تطبيق خوارزميات البحث الاعتيادية على الرسم البياني. 



## خوارزمية ميني ماكس: 

هي نوع من خوارزميات الذكاء الاصطناعي، تستخدم في الألعاب ثنائية اللاعبين مثل لعبة تيك تاك تو، لعبة الداما، الشطرنج ولعبة انطلق. 

يُعرف هذا النوع من الألعاب باسم: لعبة محصلتها صفر؛ لأنه في التمثيل الرياضي يفوز أحد اللاعبين (+1) ويخسر الآخر (-1) أو لا يفوز أي لاعب (0). 


<img width="500" alt="Screen Shot 2022-11-04 at 12 51 12 PM" src="https://user-images.githubusercontent.com/75557453/199946436-113ae3e6-4cbf-4a26-8c87-890d907ae3dd.png">


### مثال على خوارزمية ميني ماكس: 

<img width="500" alt="Screen Shot 2022-11-04 at 1 06 35 PM" src="https://user-images.githubusercontent.com/75557453/199947289-c0933d12-18aa-4949-9862-9269dc692b42.png">

## خوارزمية الألفا-بيتا: 

تعد تقنية الفا-بيتا برونينق إحدى تقنيات البحث التي تهدف إلى تقليل عدد العقد التي تم تقييمها بواسطة خوارزمية ميني ماكس  في شجرة البحث الخاصة بها. وهي تقنية بحث متقدمة تُستخدم غالبًا للعب الآلة في الألعاب ثنائية اللاعبين. تتوقف عن متابعة اختبار الحركات عندما يتم اكتشاف بديل واحد على الأقل يوضح أن الحركة ستكون أسوأ من الحركة السابقة. 


<img width="500" alt="Screen Shot 2022-11-04 at 1 00 34 PM" src="https://user-images.githubusercontent.com/75557453/199946489-ea8f8ed0-9c4f-4199-a7d1-24461fefcda5.png">

### مثال على خوارزمية الألفا-بيتا: 

  <img width="500" alt="Screen Shot 2022-11-04 at 1 06 47 PM" src="https://user-images.githubusercontent.com/75557453/199947380-596ead8a-3afe-4948-9fbc-407265dd9eed.png">



