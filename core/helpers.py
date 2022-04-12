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
            "category": "",
            "slug": "EGF-BGE"
        }
    return [
        item for i in range(60)
    ]

def get_filters(category_name):
    return {}

def paginate_data(request, data):
    pass

def get_product_detail(sku):
    return {
        "name": "Formal Shirt Beige (EGF-BGE)",
        "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
        "offers": "10% off on all orders above 100 units\n15% off on all orders above 1000 units",
        "specification": {
                "fit": "regular fit",
                "sleeve": "full sleve",
                "color": "beige",
                "type": "formals"
            },
        "highlights": "100% CottonShirts\nRegular and Slim Fit Formal Shirts\nHands-Free washing\nRich Cotton Shirts\nSlim Fir Shirts Online",
        "options": {
            "s": 299,
            "m": 399,
            "l": 499,
            "xl": 599,
            "xxl": 699
        },
        "lowest": 299,
        "sku": "EGF-BGE"

    }

def get_cart_items():
    return {
        "cart_items": [
            {
                "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                "sku": "EGF-BGE",
                "option": "s",
                "cost": "299",
                "quantity": "1",
                "name": "Forma Shirt Beige"
            },
            {
                "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                "sku": "EGF-BGE",
                "option": "m",
                "cost": "399",
                "quantity": "1",
                "name": "Forma Shirt Beige"
            },
            {
                "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                "sku": "EGF-BGE",
                "option": "l",
                "cost": "499",
                "quantity": "1",
                "name": "Forma Shirt Beige"
            },
            {
                "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                "sku": "EGF-BGE",
                "option": "xl",
                "cost": "599",
                "quantity": "1",
                "name": "Forma Shirt Beige"
            },
            {
                "url": "https://idea-unbox1.s3.ap-south-1.amazonaws.com/sku_images/EGF-LBE.jpg",
                "sku": "EGF-BGE",
                "option": "xxl",
                "cost": "799",
                "quantity": "1",
                "name": "Forma Shirt Beige"
            },
        ],
        "item_count": 5,
        "price": 2595.0,
        "discount": 0.0,
        "total": 2595.0
    }
