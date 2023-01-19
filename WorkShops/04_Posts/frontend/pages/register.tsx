import Head from "next/head";
import React, { useState } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import useAuth from "../hooks/useAuth";
import { RegisterType } from "../types";

type Props = {};

const register = (props: Props) => {
  const { registerFunc } = useAuth();
  // useForm --> form doğrulama için
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterType>();

  // https://react-hook-form.com/get-started/
  // onSubmit'i neden oluşturduk. Yukardaki link'den ulaşılabilir.
  const onSubmit: SubmitHandler<RegisterType> = async (data) => {
    await registerFunc(data);
  };

  return (
    <div>
      <Head>
        <title>Register</title>
      </Head>

      <div className="flex  justify-center items-center h-screen">
        <form
          className=" flex flex-col gap-6 p-6"
          onSubmit={handleSubmit(onSubmit)}
        >
          <input
            type="text"
            placeholder="Username"
            {...register("username", { required: true })}
          />
          {errors.username && <p>Girmek Zorunlu</p>}
          <input
            type="text"
            placeholder="Email"
            {...register("email", { required: true })}
          />
          <input
            type="text"
            placeholder="First Name"
            {...register("first_name")}
          />
          <input
            type="text"
            placeholder="Last Name"
            {...register("last_name")}
          />
          <input
            type="text"
            placeholder="Password"
            {...register("password", { required: true })}
          />
          <input
            type="text"
            placeholder="Password Again"
            {...register("password2", { required: true })}
          />
          <button type="submit">Register</button>
        </form>
      </div>
    </div>
  );
};

export default register;
