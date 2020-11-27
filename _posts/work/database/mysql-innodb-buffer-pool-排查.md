show status like 'innodb_buffer_pool_read%';

SELECT @@innodb_buffer_pool_size/1024/1024/1024;


-- select * from sys.x$memory_by_host_by_current_bytes   ;
-- select * from sys.x$memory_by_thread_by_current_bytes ;
-- select * from sys.x$memory_by_user_by_current_bytes   ;
-- select * from sys.x$memory_global_by_current_bytes    ;
-- select * from sys.x$memory_global_total               ;
-- -- select event_name,current_alloc,high_alloc from sys.memory_global_by_current_bytes where current_count > 0;
-- 
-- 
-- SELECT @@innodb_buffer_pool_size/1024/1024/1024;
show status like 'innodb_buffer_pool_read%';