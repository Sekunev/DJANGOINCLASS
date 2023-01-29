import { useRouter } from "next/router";
import React, { useEffect } from "react";
import Product from "../components/Product";
import useFetchData from "../hooks/useFetchData";

type Props = {};

const dashboard = (props: Props) => {
  const router = useRouter();
  const { products, loading, fetchAllData } = useFetchData();

  useEffect(() => {
    fetchAllData();
  }, []);

  return (
    <div>
      <button
        className="bg-pink-500 py-3 px-8 mt-4 rounded text-sm font-semibold hover:bg-opacity-75 ml-5"
        onClick={() => router.push("/addproduct")}
      >
        Add Product
      </button>
      <div className="flex flex-wrap items-center justify-center mt-20 gap-10">
        {products
          .sort((a, b) => b.id - a.id)
          .map((item) => (
            <Product item={item} key={item.id} />
          ))}
      </div>
    </div>
  );
};

export default dashboard;
