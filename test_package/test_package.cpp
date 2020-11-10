#include <restinio/all.hpp>

struct my_traits : public restinio::default_single_thread_traits_t
{
	static constexpr bool use_connection_count_limiter = true;
};

int main()
{
	restinio::on_this_thread<my_traits>()
		.port(8080)
		.address("localhost")
		.max_parallel_connections(128u)
		.incoming_http_msg_limits(
			restinio::incoming_http_msg_limits_t{}
				.max_url_size(8000u)
				.max_field_name_size(2000u)
				.max_field_value_size(4000u)
		)
		.request_handler([](auto req) {
			return req->create_response().set_body("Hello, World!").done();
		});

	return 0;
}
