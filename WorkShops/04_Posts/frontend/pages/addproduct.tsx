import { useRouter } from "next/router";
import { useForm, SubmitHandler } from "react-hook-form";
import useFetchData from "../hooks/useFetchData";
import { ProductType } from "../types";

const addproduct = () => {
  const { addProduct, loading } = useFetchData();
  const router = useRouter();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ProductType>();

  const onSubmit: SubmitHandler<ProductType> = async (data) => {
    await addProduct(data);
    router.push("/dashboard");
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="flex flex-col justify-center items-center gap-4 h-screen"
    >
      <input
        className="registerInput"
        type="text"
        placeholder="* Name"
        {...register("name", { required: true })}
      />
      <input
        className="registerInput"
        type="text"
        placeholder="* Brand"
        {...register("brand", { required: true })}
      />
      <input
        className="registerInput"
        type="number"
        placeholder="Amount"
        {...register("amount")}
      />
      <input
        className="registerInput"
        type="number"
        placeholder="Vote"
        {...register("vote")}
      />
      <input
        className="registerInput"
        type="number"
        placeholder="Rating"
        {...register("rating")}
      />

      <button className="submitButton px-10 py-2.5" type="submit">
        Add
      </button>
    </form>
  );
};

export default addproduct;
