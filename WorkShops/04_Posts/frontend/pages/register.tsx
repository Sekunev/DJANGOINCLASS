import Head from "next/head";
import React, { useState } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import useAuth from "../hooks/useAuth";
import { RegisterType } from "../types";

type Props = {};

const register = (props: Props) => {
  const { registerFunc, errorMessage } = useAuth();
  // useForm --> form doğrulama için
  console.log(errorMessage);
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
          {errorMessage?.username?.map((item, index) => (
            <p key={index}>{item}</p>
          ))}
          <input
            type="text"
            placeholder="Email"
            {...register("email", { required: true })}
          />
          {errorMessage?.email?.map((item, index) => (
            <p key={index}>{item}</p>
          ))}
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
          {errorMessage?.password?.map((item, index) => (
            <p key={index}>{item}</p>
          ))}
          <input
            type="text"
            placeholder="Password Again"
            {...register("password2", { required: true })}
          />
          {errorMessage?.password2?.map((item, index) => (
            <p key={index}>{item}</p>
          ))}
          <button type="submit">Register</button>
        </form>
      </div>
    </div>
  );
};

export default register;
