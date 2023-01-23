import Head from "next/head";
import React, { useState } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import Loader from "../components/Loader";
import useAuth from "../hooks/useAuth";
import { RegisterType } from "../types";
import { motion } from "framer-motion";

type Props = {};

const register = (props: Props) => {
  const { registerFunc, errorMessage, loading } = useAuth();
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
      <motion.div
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        className="flex justify-center items-center h-screen"
      >
        <form
          className=" flex flex-col gap-10"
          onSubmit={handleSubmit(onSubmit)}
        >
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Username"
              className="registerInput"
              {...register("username", { required: true })}
            />
            {errorMessage?.username?.map((item, index) => (
              <p className="errorMessage" key={index}>
                * {item}
              </p>
            ))}
          </div>
          <div className="inputDiv">
            <input
              type="email"
              placeholder="Email"
              className="registerInput"
              {...register("email", { required: true })}
            />
            {errorMessage?.email?.map((item, index) => (
              <p className="errorMessage" key={index}>
                * {item}
              </p>
            ))}
          </div>
          <div className="inputDiv">
            <input
              type="text"
              placeholder="First Name"
              className="registerInput"
              {...register("first_name")}
            />
          </div>
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Last Name"
              className="registerInput"
              {...register("last_name")}
            />
          </div>
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Password"
              className="registerInput"
              {...register("password", { required: true })}
            />
            {errorMessage?.password && (
              <p className="errorMessage">* {errorMessage.password[0]} </p>
            )}
          </div>
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Password Again"
              className="registerInput"
              {...register("password2", { required: true })}
            />
            {errorMessage?.password2 && (
              <p className="errorMessage">* {errorMessage.password2[0]} </p>
            )}
          </div>
          <button type="submit" className="submitButton">
            {loading ? <Loader color="#bcc" /> : "register"}
          </button>
        </form>
      </motion.div>
    </div>
  );
};

export default register;
