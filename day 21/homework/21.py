<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS კუთვნილებები</title>
    <style>
        p {
            font-size: 16;
            font-weight: normal;
            color: black;
            background-color: lightgray;
            text-align: left;
            border: 2 solid gray;
            padding: 10;
            margin: 10 0;
        }

        /* ცალკე პარაგრაფები რომ ჰქონდეს განსხვავებული სტილი */
        .p1 {
            font-size: 18;
            font-weight: bold;
            color: red;
            background-color: yellow;
            text-align: center;
            border: 3 solid red;
        }

        .p2 {
            font-size: 20;
            font-weight: lighter;
            color: green;
            background-color: lightblue;
            text-align: right;
            border: 2 dashed green;
        }

        .p3 {
            font-size: 14;
            font-weight: bold;
            color: blue;
            background-color: pink;
            text-align: justify;
            border: 2 dotted blue;
        }

        .p4 {
            font-size: 22;
            font-weight: normal;
            color: purple;
            background-color: lightgreen;
            text-align: center;
            border: 4 double purple;
        }

        .p5 {
            font-size: 12;
            font-weight: bolder;
            color: orange;
            background-color: gray;
            text-align: left;
            border: 1 solid black;
        }
    </style>
</head>
<body>

    <p class="p1">ეს არის პირველი პარაგრაფი, სადაც გამოყენებულია განსხვავებული სტილი: დიდი ზომის წითელი ტექსტი ყვითელ ფონზე, ცენტრალური განლაგებით და წითელი გრაფიკის ფორმატით.</p>

    <p class="p2">ეს არის მეორე პარაგრაფი, სადაც გამოყენებულია სხვადასხვა სტილი: საშუალო ზომის მწვანე ტექსტი მუქი ცისფერში, მარჯვენა განლაგებით და მწვანე პუნქტირებული ხაზით.</p>

    <p class="p3">ეს არის მესამე პარაგრაფი, რომელსაც აქვს პატარა ზომის ლურჯი ტექსტი ვარდისფერ ფონზე, განმაზღვრული ტექსტი და ლურჯი წერტილოვანი საზღვრით.</p>

    <p class="p4">ეს არის მეოთხე პარაგრაფი, სადაც გამოყენებულია დიდი ზომის იასამნისფერი ტექსტი მსუბუქად მწვანე ფონზე, ცენტრალური განლაგებით და იასამნისფერი ორმაგი საზღვრით.</p>

    <p class="p5">ეს არის მეხუთე პარაგრაფი, სადაც გამოყენებულია ძალიან პატარა ზომის ნარინჯისფერი ტექსტი მუქი ნაცრისფერ ფონზე, მარცხნიდან განლაგებით და შავი საზღვრით.</p>

</body>
</html>
