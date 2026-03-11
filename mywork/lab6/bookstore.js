// Task 2: use database
// use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
    { name: "Jane Austen" },
    { $set: { birthday: "1775-12-16" } }
  )

// Task 5: insert four more authors
  db.authors.insertMany([
    {
      name: "Mark Twain",
      nationality: "American",
      bio: {
        short: "American writer, humorist, and lecturer.",
        long: "Mark Twain, born Samuel Langhorne Clemens, was an American writer known for his wit and satire. His works include The Adventures of Tom Sawyer and Adventures of Huckleberry Finn, which are considered classics of American literature."
      },
      birthday: "1835-11-30"
    },
    {
      name: "Gabriel Garcia Marquez",
      nationality: "Colombian",
      bio: {
        short: "Colombian novelist and Nobel Prize winner.",
        long: "Gabriel Garcia Marquez was a Colombian novelist and journalist, widely considered one of the most significant authors of the 20th century. He was known for popularizing magical realism, especially in his famous novel One Hundred Years of Solitude."
      },
      birthday: "1927-03-06"
    },
    {
      name: "Haruki Murakami",
      nationality: "Japanese",
      bio: {
        short: "Japanese writer known for surreal and contemporary fiction.",
        long: "Haruki Murakami is a Japanese novelist whose works blend pop culture, magical realism, and philosophical themes. His novels such as Norwegian Wood, Kafka on the Shore, and 1Q84 have gained international acclaim."
      },
      birthday: "1949-01-12"
    },
    {
      name: "Charles Dickens",
      nationality: "British",
      bio: {
        short: "English writer and social critic.",
        long: "Charles Dickens was an English novelist and social critic who created some of the world's best-known fictional characters. His works, including Oliver Twist, A Christmas Carol, and Great Expectations, highlighted social issues in Victorian England."
      },
      birthday: "1812-02-07"
    }
  ])
  

// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })