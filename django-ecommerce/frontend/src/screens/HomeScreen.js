import React, {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";
import {Col, Row} from 'react-bootstrap'
import Product from '../components/Product'
import {listProducts} from "../actions/productActions";

function HomeScreen() {
    // const [p, setProducts] = useState([])
    const dispatch = useDispatch()
    const productList = useSelector(state => state.productList);
    // const productList = useSelector(state => state.product)
    const {error, loading, products} = productList;


    useEffect(() => {

        dispatch(listProducts())
    }, [])
    //
    // const products = [];


    return (
        <div>
            <h1>Latest Products</h1>
            <Row>
                {products.map(product => (
                    <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                        <Product product={product}/>
                    </Col>
                ))}
            </Row>
        </div>
    )
}

export default HomeScreen