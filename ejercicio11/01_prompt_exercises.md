# Exercises

https://github.com/tamasma/master-ia-tajamar/tree/main/Prompt-Engineering-Exercises

In this document, you find a few exercises for practicing prompt engineering. For each exercise, you'll get some input text and then an expected completion. You task is to write the prompt to achieve the expected completion.
___

## :question: Exercise 1 - German Translation

* Exercise: Write a prompt that generates the expected completion
* Input text: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Expected completion: `Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.`
![alt text](images\image-1.png)

___

## :question: Exercise 2 - Negation

* Exercise: Write a prompt that generates the expected completion
* Input text: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Expected completion: `I was not enjoying the sun, and then a huge cloud did not come and cover the sky.`
![alt text](images\image-2.png)

___

## :question: Exercise 3 - Classification

* Exercise: Write a prompt that generates the expected completion
* Input text: `Not much to write about here, but it does exactly what it's supposed to. filters out the pop sounds. now my recordings are much more crisp. it is one of the lowest prices pop filters on amazon so might as well buy it, they honestly work the same despite their pricing.`
* Expected completion (or similar):
  ```
  Positive: 0.75
  Neutral: 0.20
  Negative: 0.05
  ```
![alt text](images\image-3.png)
___

## :question: Exercise 4 - E-Mail Summarization

* Exercise: Write a prompt that generates the expected completion
* Input text: Use your own email...
* Expected completion (or similar):
  ```
  Summary: XYZ
  Open Questions: XYZ
  Action Items: XYZ
  ```
![alt text](images\image-4.png)

___

## :question: Exercise 5 - Rewriting

* Exercise: Write a prompt that generates the expected completion
* Input text: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Expected completion: `She was enjoying the sun, but then a huge cloud came and covered the sky.`
![alt text](images\image-5.png)
___

## :question: Exercise 6 - Multiple Tasks

* Exercise: Write a prompt that generates the expected completion
* Input text: `I was enjoying the sun, but then a huge cloud came and covered the sky.`
* Expected completion:
  ```
  {
      "translated": "Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.",
      "negated": "I was not enjoying the sun, and no huge cloud came and covered the sky.",
      "third_person": "She was enjoying the sun, but then a huge cloud came and covered the sky."
  }
  ```
![alt text](images\image-6.png)
___

## :question: Exercise 7 - Data extraction to JSON

* Exercise: Write a prompt that generates the expected completion
* Input text:
  ```
  Hello, my name is Mateo Gomez. I lost my Credit card on August 17th, and I would like to request its cancellation. The last purchase I made was of a Chicken parmigiana dish at Contoso Restaurant, located near the Hollywood Museum, for $40. Below is my personal information for validation:
  Profession: Accountant
  Social Security number is 123-45-6789
  Date of birth: 9-9-1989
  Phone number: 949-555-0110
  Personal address: 1234 Hollywood Boulevard Los Angeles CA
  Linked email account: mateo@contosorestaurant.com
  Swift code: CHASUS33XXX
  ```
* Expected completion:
  ```
  {
      "reason": "Lost card",
      "classified_reason": "lost_card",
      "name": "Mateo Gomez",
      "ssn": "123-45-6789",
      "dob": "09/09/1989"
  }
  ```
![alt text](images\image-7.png)
___

## :question: Exercise 8 - Fashion product description

* Exercise: Write a prompt that generates the expected completion
* Input text:
  ```
  Season: Winter
  Style: Sweater
  Gender: Female
  Target group: Teenager
  Material: Cotton
  ```
* Expected completion (or similar):
  ```
  Stay warm and stylish this winter with our cozy cotton sweaters, perfect for the fashion-forward teenager. Refresh your wardrobe with the latest winter styles from our collection.
  ```
![alt text](images\image-8.png)


___

## :question: Exercise 9 - Write a Blog Post

* Exercise: Write a blog post about a topic of your choice
* Input text: You choose
* Expected completion: a blogpost with hashtages
Prompt
```
Write a blog post about travelling to Thailand and give me hashtages
```
![alt text](images\image-9.png)
ChatGPT Answer
```
Exploring Thailand: A Traveler’s Paradise

Thailand, often referred to as the "Land of Smiles," is one of the most vibrant and diverse countries in Southeast Asia. Whether you’re a history buff, nature lover, adventure seeker, or beach enthusiast, Thailand has something for everyone. From bustling cities to serene islands, and ancient temples to lush jungles, every corner of this beautiful country tells a unique story. Here’s your guide to experiencing Thailand’s highlights and making the most of your trip!

1. Bangkok: The City That Never Sleeps
Start your adventure in Thailand’s capital, Bangkok – a city that perfectly blends modernity and tradition. The towering skyscrapers, neon lights, and busy streets filled with tuk-tuks and street vendors are iconic. Yet, amidst the chaos, you’ll find serene temples, including the breathtaking Wat Arun and Wat Phra Kaew (Temple of the Emerald Buddha). Don’t miss a boat ride along the Chao Phraya River, which offers stunning views of the city’s skyline and traditional wooden houses.

The Chatuchak Market is perfect for shopping, while the Khao San Road offers vibrant nightlife. For a calmer experience, spend an afternoon at Lumphini Park, a green oasis in the heart of the city.

2. Chiang Mai: The Heart of Northern Thailand
For a completely different vibe, head north to Chiang Mai. Known for its rich cultural heritage, this city is home to hundreds of ancient temples like Wat Phra That Doi Suthep, which offers panoramic views of the surrounding mountains. Chiang Mai is also the gateway to nearby hill tribes, where you can learn about traditional ways of life.

Adventure enthusiasts will love the Elephant Nature Park, an ethical sanctuary where you can spend time with rescued elephants. Or, take a trekking tour through the scenic mountains and explore the stunning waterfalls of Doi Inthanon National Park.

3. Krabi: Beaches, Caves, and Limestone Cliffs
No trip to Thailand is complete without a visit to its famous beaches. Krabi is one of the country’s most popular destinations for its pristine beaches, turquoise waters, and dramatic limestone cliffs. Whether you’re exploring the picturesque Railay Beach, hiking up to Phi Phi Viewpoint, or island-hopping to Koh Phi Phi and Koh Lanta, there’s no shortage of natural beauty here.

For an unforgettable experience, take a kayaking tour through the Ao Thalane mangrove forests or visit the secluded Phra Nang Cave Beach with its crystal-clear water and stunning cave.

4. Koh Samui: Relaxation and Nightlife in Paradise
If you're looking for the perfect island escape, Koh Samui should be at the top of your list. Known for its palm-lined beaches and luxury resorts, this island is perfect for a laid-back vacation. Chaweng Beach offers vibrant nightlife with its bars and clubs, while Lamai Beach is quieter and ideal for relaxation.

For a bit of culture, visit the Big Buddha statue or take a trip to Ang Thong National Marine Park for a day of snorkeling, kayaking, and exploring hidden lagoons.

5. Ayutthaya: A Journey Back in Time
For history lovers, Ayutthaya, the ancient capital of the Kingdom of Siam, is a must-see. This UNESCO World Heritage site is home to impressive ruins, such as the Wat Phra Si Sanphet and Wat Mahathat, where you can see the famous Buddha head entwined in tree roots. Take a boat tour around the island to see the temples from a different perspective or hire a bicycle to explore the archaeological park.

6. Thai Cuisine: A Feast for the Senses
No trip to Thailand is complete without tasting the country’s world-renowned cuisine. Street food is a huge part of Thai culture, and you’ll find everything from Pad Thai and Tom Yum soup to Som Tum (papaya salad) and Mango Sticky Rice. Don’t forget to try Satay, Roti, and Green Curry as well! If you’re feeling adventurous, sample Durian, the famously stinky yet delicious fruit.

7. The Culture and People
What truly sets Thailand apart is its welcoming and warm-hearted people. Thai culture is deeply rooted in respect for others, with Buddhism playing an important role in daily life. You’ll see this reflected in the country’s stunning temples, festive celebrations, and the serene attitude of the locals.

If you're in Thailand during the Songkran Festival, celebrate the Thai New Year with a massive nationwide water fight! Or experience the beauty of Loy Krathong, where thousands of lit lanterns are released into the night sky.

Final Tips for Your Thailand Trip:
Respect local customs: Always remove your shoes when entering temples or homes, and dress modestly when visiting sacred sites.
Stay hydrated: Thailand’s tropical climate can be hot and humid, so drink plenty of water and carry sunscreen.
Transportation: Use tuk-tuks or motorbikes for short distances, but be sure to negotiate the price before getting in.
Conclusion: Why Thailand is a Must-Visit Destination
Thailand is a destination that offers so much more than just picturesque beaches. Whether you’re exploring the cultural riches of Chiang Mai, the modernity of Bangkok, or the tranquility of its islands, you’ll find that Thailand’s beauty and charm are unmatched. So pack your bags, and get ready to create unforgettable memories in the Land of Smiles!

Hashtags to Share Your Thailand Adventure:
#VisitThailand #LandOfSmiles #ThailandTravel #ExploreThailand #AmazingThailand #ThailandBeaches #BangkokAdventures #ChiangMai #KohSamui #ThaiCuisine #TravelGoals #Wanderlust #TukTukLife #ThailandVibes #AdventureAwaits #IslandHopping #TravelDiaries
```


___

## :question: Exercise 10 - Call Center

* Exercise: Analyze a call center conversation
* Input text:
  ```
  Employee: "Hello, this is Julia Schreider from Contoso Company. How can I help you today?"
  Customer: "Hi, I am Carsten Mueller. I ordered a package 10 days ago, on February 10th, and it was supposed to arrive in maximum 5 business days. I have called three times already and nobody could provide any more information. I want to know where the package is and I want the problem to be solved immediately. This is the worst service I had for a long time!"
  Employee: "I apologize for the inconvenience, Mr. Mueller. I understand your frustration and I'm here to help. Can you please provide me with your order number so I can look into this for you?"
  Customer: "Yes, it's ACZ456789."
  Employee: "Thank you. I'm looking into it now. Can you please hold for a few minutes while I check the status of your package?"
  Customer: "Okay."
  Employee: "Thank you for your patience. I am sorry to inform you that I am unable to find the status of your package. It appears to have left the sending address, but no up-to-date status on the current location. I will further investigate your case and get back to you as soon as possible via phone call. Could you please provide me your contact information?"
  Customer: "Ah not again. Anyway, my phone number is +4911112223344."
  Employee: "I apologize again for the inconvenience. Is there anything else I can help you with today?"
  Customer: "No."
  Employee: "Thank you. Have a great day!"
  ```
* Expected completion:
  ```
  {
      "classified_reason": "lost_package",
      "resolve_status": "unresolved",
      "call_summary": "Customer ordered package 10 days ago and has not received it yet.",
      "customer_name": "Carsten Mueller",
      "employee_name": "Julia Schreider",
      "order_number": "ACZ456789",
      "customer_contact_nr": "+4911112223344",
      "new_address": "N/A",
      "sentiment_initial": ["angry", "frustrated"],
      "sentiment_final": ["calm"],
      "satisfaction_score_initial": 0,
      "satisfaction_score_final": 5,
      "eta": "N/A",
      "action_item": ["track_package", "inquire_package_status", "contact_customer"]
  }
  ```
![alt text](image-10.png)
![alt text](image-11.png)
___

## :question: Exercise 11 - Few-shot learning

* Exercise: Write a few-shot learned prompt that classifies a movie summary.
* Data samples:
  ```
  Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive.
  ['Action', 'Adventure', 'Science Fiction’]

  A botched store robbery places Wonder Woman in a global battle against a powerful and mysterious ancient force that puts her powers in jeopardy.
  ['Action', 'Adventure', 'Fantasy']

  After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos' actions and restore order to the universe once and for all, no matter what consequences may be in store.
  ['Adventure', 'Science Fiction', 'Action']

  A widowed new dad copes with doubts, fears, heartache and dirty diapers as he sets out to raise his daughter on his own. Inspired by a true story.
  ['Drama', 'Family', 'Comedy’]

  New data:
  Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.
  ```
* Expected completion: Classification of the new data point
![alt text](image-12.png)


___

## :question: Exercise 12 - NL to SQL

* Exercise: Write a prompt that generates the expected SQL statement
* Table information:
  * Table: customer // Columns: firstname, name, customer_id, address
  * Table: orders // Columns: order_id, customer_id, product_id, product_amount
  * Table: products // Columns: product_id, price, name, description
* Expected completion: a query that returns the top 10 orders and show the customer name

```sql
SELECT 
    c.firstname, 
    c.name AS customer_name, 
    o.order_id, 
    o.product_id, 
    o.product_amount
FROM 
    orders o
JOIN 
    customer c ON o.customer_id = c.customer_id
ORDER BY 
    o.order_id DESC
LIMIT 10;

```

![alt text](image-13.png)
![alt text](image-14.png)


