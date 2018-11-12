---
layout: post
title:  "Java Spring MVC"
rootCate: "work"
categories:
- Java
tags:
- work
- Java
- Spring MVC
---

> StartTime: 2015-08-26,ModifyTime:2017-01-01
<!---more--->

> 主要的参考资料：
http://www.cnblogs.com/zemliu/archive/2013/08/06/3239718.html
http://www.iteye.com/problems/82189
http://bbs.csdn.net/topics/390239820/
http://blog.csdn.net/huaishuming/article/details/39676627
http://www.iteye.com/problems/82189     题目：ssh中把service注入到action，为什么不能注入service的实现类
http://blog.csdn.net/ye1992/article/details/19972041
http://blog.csdn.net/ye1992/article/details/19971467

以下都需要在 XML 配置文件中启用Bean 的自动扫描功能，这可以通过<context:component-scan/>实现。这样，我们就不再需要在 XML 中显式使用 <bean/> 进行Bean 的配置。Spring 在容器初始化时将自动扫描 base-package 指定的包及其子包下的所有 class文件，所有标注了 的类都将被注册为 Spring Bean。

@Repository注解便属于最先引入的一批，它用于将数据访问层 (DAO 层 ) 的类标识为 Spring Bean。@Repository 只能标注在 DAO 类原因：Spring本身提供了一个丰富的并且是与具体的数据访问技术无关的数据访问异常结构，用于封装不同的持久层框架抛出的异常，使得异常独立于底层的框架。

Spring2.5之后增加了三个@Component、@Service、@Constroller。
@Component 是一个泛化的概念，仅仅表示一个组件 (Bean) ，可以作用在任何层次。例子@Component("boss")。

@Service 通常作用在业务层，但是目前该功能与 @Component 相同。

@Constroller 通常作用在控制层，但是目前该功能与 @Component 相同。

@Autowired，对成员变量使用，可以将它们的 setter 方法从类中删除。@Autowired 可以对成员变量、方法以及构造函数进行注释。自动注入的策略是根据变量的类型，也就是byType 。此时Spring 容器中匹配的候选 Bean 数目必须有且仅有一个，否则Spring 容器将抛BeanCreationException 异常。在开发期或测试期（如为了快速启动 Spring 容器，仅引入一些模块的 Spring 配置文件），可以用@Autowired(required = false) ，在找不到匹配 Bean 时也不报错。和找不到一个类型匹配 Bean 相反的一个错误是：如果 Spring 容器中拥有多个候选 Bean，Spring 容器在启动时也会抛出 BeanCreationException 异常。通过在XML中配置AutowiredAnnotationBeanPostProcessor ，它将扫描 Spring 容器中所有 Bean，当发现 Bean 中拥有@Autowired 注释时就找到和其匹配（默认按类型匹配）的 Bean，并注入到对应的地方中去。

@Qualifier("office") 中的 office 是 Bean 的名称，所以 @Autowired和@Qualifier 结合使用时，转变成 byName 了。 ，而@Qualifier 的标注对象是成员变量、方法入参、构造函数入参。
@RequestParam注解可以用来提取名为“number”的String类型的参数，并将之作为输入参数传入。 例如public void show(@RequestParam("number") String number, Map<String, Object> model) { }。属性required=false或者true可以用来要求@RequestParam配置的前端参数是否一定要传给后台 。

@RequestMapping是一个用来处理请求地址映射的注解，可用于类或方法上。用于类上，表示类中的所有响应请求的方法都是以该地址作为父路径。
value：     指定请求的实际地址，指定的地址可以是URI Template 模式（后面将会说明）；
method：  指定请求的method类型， GET、POST、PUT、DELETE等。

@Scope，它能够配合这四个注解在标注 Bean 的同时能够指定 Bean 的作用域。与通过 XML 配置的 Spring Bean 一样，通过上述注解标识的Bean，其默认作用域是"singleton"。使用该注解时只需提供作用域的名称就可以了。例如：
	@Scope("prototype")
	@Repository
	public class Demo { … }
	当一个 Bean 被自动检测到时，会根据那个扫描器的 BeanNameGenerator 策略生成它的Bean名称。默认情况下，对于使用了 name 属性的 注解，会把 name 值作为 Bean 的名字。如果这个注解不使用 name属性或是其他被自定义过滤器发现的组件，默认 Bean 名称会是小写开头的非限定类名。


Spring Web MVC支持多种类型的控制器，比如实现Controller接口，从Spring2.5开始**支持注解方式的控制器**（如@Controller、@RequestMapping、@RequestParam、@ModelAttribute等），我们也可以**实现自己的控制器**（只需要定义相应的HandlerMapping和HandlerAdapter即可）。还有部分公司使用继承Controller接口实现方式。

dao service接口的注入      service中要注入dao接口还是dao实现类，要看业务需求。因为当一个service需要多个dao类的方法时候，注入dao接口可以尽可能避免代码冗余（例如大量不同service的类的实例化）。

把DAO实现类注入到service实现类中，把service的接口(注意不要是service的实现类)注入到action中，注入时不要new 这个注入的类，因为spring会自动注入，如果手动再new的话会出现错误，然后属性加上

@Autowired后不需要getter()和setter()方法，Spring也会自动注入。还有一种情况也不需要实例化，应该是其他的注解。

在spring的配置文件里面可以使用base-package="*"表示全部的类。这一点和前一篇文章对注解的xml文件配置结合起来看。

在接口前面标上@Autowired和@Qualifier注释使得接口可以被容器注入，当接口存在两个实现类的时候必须指定其中一个来注入，使用实现类首字母小写的字符串来注入。
