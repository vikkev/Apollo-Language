; Código LLVM IR gerado para Apollo

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
  %0 = alloca i32
  store i32 0, i32* %0
  %1 = alloca i32
  store i32 0, i32* %1
  %2 = alloca i32
  store i32 0, i32* %2
  %3 = getelementptr inbounds [26 x i8], [26 x i8]* @.str0, i32 0, i32 0
  %4 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %4, i8* %3)
  %5 = getelementptr inbounds [2 x i8], [2 x i8]* @.str2, i32 0, i32 0
  call i32 (i8*, ...) @scanf(i8* %5, i32* %0)
  %6 = getelementptr inbounds [25 x i8], [25 x i8]* @.str3, i32 0, i32 0
  %7 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %7, i8* %6)
  %8 = getelementptr inbounds [2 x i8], [2 x i8]* @.str2, i32 0, i32 0
  call i32 (i8*, ...) @scanf(i8* %8, i32* %1)
  %9 = load i32, i32* %0
  %10 = load i32, i32* %1
  %11 = add i32 %9, %10
  store i32 %11, i32* %2
  %12 = getelementptr inbounds [10 x i8], [10 x i8]* @.str4, i32 0, i32 0
  %13 = getelementptr inbounds [3 x i8], [3 x i8]* @.str1, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %13, i8* %12)
  %14 = load i32, i32* %2
  %15 = getelementptr inbounds [3 x i8], [3 x i8]* @.str5, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %15, i32 %14)
  ret i32 0
}

@.str0 = private unnamed_addr constant [26 x i8] c"Digite o primeiro número:\00"
@.str1 = private unnamed_addr constant [6 x i8] c"%s\5C0A\00"
@.str2 = private unnamed_addr constant [3 x i8] c"%d\00"
@.str3 = private unnamed_addr constant [25 x i8] c"Digite o segundo número:\00"
@.str4 = private unnamed_addr constant [10 x i8] c"A soma é:\00"
@.str5 = private unnamed_addr constant [6 x i8] c"%d\5C0A\00"