def get_top_apparels():
    return [
            [
                {
                    "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Formal Shirt Biege",
                    "id": 1
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(18).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 2
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(35).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 3
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(35).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 3
                },
            ],
            [
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/City/4-col/img%20(47).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 4
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/City/4-col/img%20(48).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 5
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Food/4-col/img%20(53).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 6
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Food/4-col/img%20(53).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 6
                },
            ],
            [
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Food/4-col/img%20(45).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 7
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Food/4-col/img%20(51).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 8
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(35).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 9
                },
                {
                    "url": "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(35).jpg",
                    "text": "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    "heading": "Card title",
                    "id": 9
                },
            ],

        ]


def get_catalogue_items(categoy_name, filters):
    item = {
            "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
            "name": "Formal Light Beige",
            "price_point": "299",
            "id": 1,
            "category": ""
        }
    return [
        item for i in range(60)
    ]

def get_filters(category_name):
    return {}

def paginate_data(request, data):
    pass
